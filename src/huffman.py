import os
import heapq
import json

class HuffmanNode:
    """
    Node class for building the Huffman Tree.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue to compare nodes based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    """
    Core class containing all logic for Huffman Compression and Decompression.
    """
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # ==========================================
    # COMPRESSION FUNCTIONS
    # ==========================================
    
    def make_frequency_dict(self, text):
        """Calculates and returns the frequency of each character in the text."""
        frequency = {}
        for char in text:
            if not char in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def make_heap(self, frequency):
        """Builds a min heap (priority queue) from the frequency dictionary."""
        for key in frequency:
            node = HuffmanNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        """Builds the Huffman Tree by merging nodes from the heap."""
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        """Recursive helper function to traverse tree and assign binary codes."""
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        """Generates Huffman codes and reverse mappings."""
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        """Replaces characters in text with their binary Huffman codes."""
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        """Pads the encoded text to ensure its length is a multiple of 8 bits."""
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        # Store padding info in the first 8 bits (1 byte)
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        """Converts the padded binary string into an array of bytes."""
        if len(padded_encoded_text) % 8 != 0:
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b

    def compress(self, output_path):
        """Executes the full compression pipeline."""
        with open(self.path, 'r+', encoding='utf-8') as file, open(output_path, 'wb') as output:
            text = file.read()
            if not text:
                print("File is empty.")
                return

            # Step 1-4: Generate Tree and Codes
            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            # Step 5: Encode text
            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)
            
            # Step 6: Convert to bytes
            b = self.get_byte_array(padded_encoded_text)
            
            # Write metadata (reverse mapping) so we can decompress later
            metadata = json.dumps(self.reverse_mapping)
            output.write(metadata.encode('utf-8'))
            output.write(b'\n') # Separator
            
            # Write compressed data
            output.write(bytes(b))

        return output_path

    # ==========================================
    # DECOMPRESSION FUNCTIONS
    # ==========================================

    def remove_padding(self, padded_encoded_text):
        """Removes the extra padding added during compression."""
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1*extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        """Converts the binary string back to original text using reverse mapping."""
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self, input_path, output_path):
        """Executes the full decompression pipeline."""
        with open(input_path, 'rb') as file, open(output_path, 'w', encoding='utf-8') as output:
            # Read metadata first
            metadata_line = file.readline()
            self.reverse_mapping = json.loads(metadata_line.decode('utf-8'))

            # Read remaining compressed binary data
            bit_string = ""
            byte = file.read(1)
            while len(byte) > 0:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            # Step 1: Remove padding
            encoded_text = self.remove_padding(bit_string)
            
            # Step 2: Decode using the loaded mapping
            decoded_text = self.decode_text(encoded_text)
            
            # Write decompressed data
            output.write(decoded_text)

        return output_path
