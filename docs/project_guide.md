# 📚 Project Guide: Dynamic File Compression Utility

This document contains the step-by-step explanations, virtual simulation guide, and the Github Proof-Building Strategy as requested.

## 1️⃣ Project Explanation

### What is a Dynamic File Compression Utility?
It is a software tool that reduces the size of a file on the disk without losing any information. It is "dynamic" because it reads the specific file provided by the user and generates a custom compression algorithm tailored exactly to the contents of that file.

### Why is file compression important?
- **Storage:** Saves hard drive space.
- **Bandwidth:** Faster transfer over the internet (e.g., loading web pages, downloading games).
- **Cost:** Cloud storage (like AWS S3) charges per GB. Smaller files = lower costs.

### How does it reduce file size? (Simple vs Technical)
**Simple Explanation:**
Imagine you are texting a friend. Instead of writing "Talk to you later", you write "TTYL". You assigned a shorter code to a phrase you use frequently. This utility does the exact same thing for the computer, but at the character level.

**Technical Explanation:**
Standard text files use ASCII/UTF-8 encoding where every character takes exactly 8 bits (1 byte). E.g., `A = 01000001`. 
Huffman Coding assigns *variable-length* codes. Frequent characters (like 'e') might get a 2-bit code (`10`), while rare characters (like 'z') get a 10-bit code (`1101001011`). Because frequent characters take up drastically less space, the total file size shrinks.

---

## 2️⃣ Virtual Simulation

How to simulate and test this utility for your portfolio:

1. **Create Sample Data:** Go to lipsum.com and generate 10 paragraphs of text. Save it as `input_files/large_sample.txt`.
2. **Check Original Size:** Right-click the file -> Properties to note the size in Bytes.
3. **Run Compression:** `python src/main.py compress input_files/large_sample.txt`.
4. **Capture Screenshot 1:** Take a screenshot of your terminal showing the "Compression ratio: XX% space saved."
5. **Verify Binary:** Try to open `compressed_files/large_sample.bin` in a text editor. You will see unreadable garbled symbols. This proves it is converted to raw bytes.
6. **Run Decompression:** `python src/main.py decompress compressed_files/large_sample.bin`.
7. **Verify Accuracy:** Open `decompressed_files/large_sample_recovered.txt` and verify it perfectly matches the original text.
8. **Capture Screenshot 2:** Take a side-by-side screenshot of the original file and the recovered file.

*Upload these screenshots to the `images/` folder and link them in your README.*

---

## 3️⃣ Proof Building Strategy (GitHub Upload Steps)

To make this project look like a professional, iterative build, DO NOT upload it all at once. Follow this day-wise commit plan to show a history of progress.

**Repository Name Idea:** `Dynamic-Huffman-Compressor` or `DSA-File-Compression-Engine`
**Tags:** `python`, `data-structures`, `algorithms`, `huffman-coding`, `system-programming`, `file-compression`

### Day 1: Setup and File Reading
- **Action:** Create folder structure, `main.py` skeleton, and `.gitignore`.
- **Commit Message:** `chore: initialize project structure and CLI skeleton`

### Day 2: Frequency Table and Min Heap
- **Action:** Add `HuffmanNode` class, `make_frequency_dict`, and `make_heap` methods to `src/huffman.py`.
- **Commit Message:** `feat: implement char frequency map and min heap construction`

### Day 3: Huffman Tree Generation
- **Action:** Implement `merge_nodes` and `make_codes` in `huffman.py`.
- **Commit Message:** `feat: implement huffman tree building and binary code generation`

### Day 4: Encoding and Compression Phase
- **Action:** Implement padding logic, byte array conversion, and `compress()` file writing.
- **Commit Message:** `feat: implement byte-level file compression and binary export`

### Day 5: Decoding and Decompression Phase
- **Action:** Implement padding removal, text decoding, and `decompress()` file writing.
- **Commit Message:** `feat: implement binary file decompression and tree mapping recovery`

### Day 6: Final CLI Integration and Documentation
- **Action:** Wire up `main.py` with `HuffmanCoding`, add ratio calculation, and upload `README.md`.
- **Commit Message:** `docs: add comprehensive README, CLI polish, and usage metrics`

---

## 4️⃣ Interview Preparation

When discussing this project in an interview, focus on these points:
1. **Time Complexity:** 
   - Frequency mapping: $O(N)$ where $N$ is file length.
   - Heap building: $O(U \log U)$ where $U$ is the number of *unique* characters.
   - Total Compression: $O(N \log U)$.
2. **Space Complexity:**
   - $O(U)$ for the dictionary and the Heap. Since $U$ (unique characters) is at most 256 for ASCII, space complexity is technically $O(1)$ constant overhead!
3. **Challenges Overcome:** Talk about how you handled padding (files must be saved in full 8-bit bytes, but Huffman codes don't always align to multiples of 8, requiring manual bit-padding and saving the padding length).
