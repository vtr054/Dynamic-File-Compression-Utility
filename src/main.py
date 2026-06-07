import sys
import os
from huffman import HuffmanCoding

def print_usage():
    print("========================================")
    print("  Dynamic File Compression Utility CLI  ")
    print("========================================")
    print("Usage: python src/main.py <action> <input_file>")
    print("\nActions:")
    print("  compress    - Compresses the given text file.")
    print("  decompress  - Decompresses the given binary file.")
    print("\nExamples:")
    print("  python src/main.py compress input_files/sample.txt")
    print("  python src/main.py decompress compressed_files/sample.bin")

def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    action = sys.argv[1].lower()
    input_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    filename, file_extension = os.path.splitext(os.path.basename(input_file))

    if action == "compress":
        if file_extension != '.txt':
            print("Warning: It is recommended to compress .txt files.")
            
        output_file = os.path.join("compressed_files", filename + ".bin")
        print(f"\n[INFO] Starting compression of {input_file}...")
        
        huffman = HuffmanCoding(input_file)
        huffman.compress(output_file)
        
        original_size = os.path.getsize(input_file)
        compressed_size = os.path.getsize(output_file)
        
        print("\n[SUCCESS] Compression complete!")
        print(f"Original size:    {original_size} bytes")
        print(f"Compressed size:  {compressed_size} bytes")
        
        if original_size > 0:
            ratio = (compressed_size / original_size) * 100
            print(f"Compression ratio: {100 - ratio:.2f}% space saved.")
            
        print(f"Output saved to: {output_file}\n")

    elif action == "decompress":
        if file_extension != '.bin':
            print("Warning: Expected a .bin file for decompression.")

        output_file = os.path.join("decompressed_files", filename + "_recovered.txt")
        print(f"\n[INFO] Starting decompression of {input_file}...")
        
        huffman = HuffmanCoding(input_file) # Path isn't strictly needed for decompression initialization
        huffman.decompress(input_file, output_file)
        
        print("\n[SUCCESS] Decompression complete!")
        print(f"Output saved to: {output_file}\n")

    else:
        print(f"Error: Unknown action '{action}'.")
        print_usage()

if __name__ == "__main__":
    main()
