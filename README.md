# Dynamic File Compression Utility 🗜️

![Project Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Concepts](https://img.shields.io/badge/DSA-Huffman_Coding%20%7C%20Heaps%20%7C%20Trees-orange)

A powerful, efficient, and dynamic file compression and decompression utility built entirely from scratch using **Data Structures and Algorithms (DSA)**. This tool uses **Huffman Coding** to significantly reduce the size of text files without losing any data (Lossless Compression).

---

## 📖 Project Overview

This project is an industry-oriented implementation of the classic file compression problem. It demonstrates how abstract Data Structures (like Min Heaps, Binary Trees, and Hash Maps) can be combined to solve real-world system engineering problems, such as optimizing storage and reducing network bandwidth.

### What Problem Does It Solve?
Uncompressed text files often use 8 bits (1 byte) for every character, regardless of how frequently that character appears. In large logs, books, or codebases, some characters (like `e`, `t`, space) appear constantly, while others (like `z`, `x`) rarely appear. This utility solves this inefficiency by assigning shorter bit-codes to frequent characters and longer bit-codes to rare characters, drastically reducing the overall file size.

---

## 🧠 Data Structures & Algorithms Used

1. **Hash Maps / Dictionaries (`collections.Counter`)**: Used to parse the input file and count the frequency of each character in $O(N)$ time.
2. **Min Heap / Priority Queue (`heapq`)**: Used to constantly extract the two nodes with the lowest frequencies in $O(\log N)$ time to build the Huffman Tree optimally.
3. **Binary Tree (Huffman Tree)**: The core data structure. A custom `Node` class forms a tree where leaf nodes represent characters, and the path from the root to the leaf determines the binary code.
4. **Tree Traversal (DFS)**: Used to traverse the constructed Huffman Tree to generate the final binary mappings for each character.
5. **Bit Manipulation & Padding**: Used to pack the generated variable-length binary strings into solid 8-bit bytes for file writing.

---

## ⚙️ Features

- **Lossless Compression**: 100% of the original data is recovered upon decompression.
- **Dynamic Encoding**: Generates a unique Huffman Tree optimized specifically for the exact file being compressed.
- **Embedded Metadata**: Smartly bundles the reverse-mapping dictionary header into the binary file, meaning the compressed `.bin` file is entirely standalone and does not need the original file to decompress.
- **CLI Interface**: Easy-to-use Command Line Interface.
- **Metrics Reporting**: Automatically calculates and reports the original size, compressed size, and the compression ratio.

---

## 📂 Folder Structure

```text
Dynamic-File-Compression-Utility/
│
├── input_files/          # Store your raw .txt files here
├── compressed_files/     # Compressed .bin files are saved here
├── decompressed_files/   # Restored .txt files are saved here
├── src/                  # Source Code
│   ├── huffman.py        # Core DSA Logic (Tree, Heap, Encoding)
│   └── main.py           # CLI Interface and File Handling
├── outputs/              # (Optional) Store terminal output logs here
├── images/               # Screenshots for GitHub documentation
├── docs/                 # Extended project guides and proof plans
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies
└── .gitignore            # Files to ignore in Git
```

---

## 🚀 How to Run (Installation & Usage)

### Prerequisites
- Python 3.6 or higher installed on your system.
- No external libraries required (uses Python Standard Library).

### Step 1: Clone and Setup
```bash
git clone https://github.com/your-username/Dynamic-File-Compression-Utility.git
cd Dynamic-File-Compression-Utility
```

### Step 2: Create a Sample File
Create a text file inside `input_files/` named `sample.txt` and add some text (the larger the text, the better the compression ratio).

### Step 3: Compress the File
Run the following command from the root directory:
```bash
python src/main.py compress input_files/sample.txt
```
**Expected Output:**
```text
[INFO] Starting compression of input_files/sample.txt...

[SUCCESS] Compression complete!
Original size:    1048576 bytes
Compressed size:  580000 bytes
Compression ratio: 44.69% space saved.
Output saved to: compressed_files/sample.bin
```

### Step 4: Decompress the File
Run the following command to restore the file:
```bash
python src/main.py decompress compressed_files/sample.bin
```
**Expected Output:**
```text
[INFO] Starting decompression of compressed_files/sample.bin...

[SUCCESS] Decompression complete!
Output saved to: decompressed_files/sample_recovered.txt
```

---

## 🎓 Learning Outcomes
By building this project, you will master:
- Translating theoretical DSA concepts into functional, system-level code.
- File I/O operations (reading/writing raw bytes vs. strings).
- Algorithmic thinking and code modularization.
- Advanced Python concepts (custom `__lt__` magic methods for Priority Queues, Bit manipulation).

*Created as a Proof of Work for Software Engineering & Backend roles.*
