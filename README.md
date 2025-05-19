Plagiarism Checker Using Suffix Array
Overview
This project is a plagiarism detection tool that compares two text documents by finding the longest common substrings between them. It calculates a similarity score based on the length of the longest common substring (LCS), offering a metric for determining the potential overlap between the two documents. The tool uses a Suffix Array to efficiently compare the suffixes of both documents, and detects the longest substrings that appear in both, even across different documents.

Features
Longest Common Substring (LCS) Detection: The tool finds the longest common substring between two documents.

Similarity Score: Based on the LCS, a percentage similarity score is generated.

Plagiarism Detection Report: A detailed report with the lengths of both documents, LCS length, and similarity score is produced.

Handling of Document Splits: Documents can be split using a separator to handle different documents being compared.

Requirements
Python 3.x

Standard Python libraries (os, collections, etc.)

Files
plagiarism_checker.py: The main script containing the functionality to compute the similarity score.

doc1.txt (Example): Sample text file 1 to be compared.

doc2.txt (Example): Sample text file 2 to be compared.

  ** Usage** 
Step 1: Prepare the Documents
Create or have two text files (doc1.txt and doc2.txt) that you want to compare for plagiarism. These files can be of any size but should contain plain text data.

Step 2: Modify the Paths (Optional)
Update the file paths in the script to point to the location of your documents, or leave the filenames as-is if the text files are in the same directory as the script.

Step 3: Run the Script
To run the plagiarism checker, simply execute the Python script:

python plagiarism_checker.py
Output
The script will print the following information:

Document Lengths: The number of characters in each document.

Longest Common Substring Length: The length of the longest substring common to both documents.

Similarity Score: A percentage similarity score based on the longest common substring.

Detected Common Substrings: A list of common substrings that contribute to the similarity score.

Example output:
=======================================================================
                         PLAGIARISM CHECKER REPORT
=======================================================================
Document 1 Length:               1500 characters
Document 2 Length:               1200 characters
Longest Common Substring Length: 45 characters
Similarity Score:                23.80%
-----------------------------------------------------------------------
Detected Longest Common Substring(s):
  1. "The quick brown fox"
=======================================================================
                 Analysis complete using Suffix Array
=======================================================================
How It Works
Building the Suffix Array:

The script first combines both documents into one, separating them with a unique separator string.

The suffix array is built by sorting all suffixes of this combined text.

Longest Common Substring Search:

The script compares suffixes from different documents in the suffix array and computes the length of the longest common prefix (LCP) for each pair of suffixes.

Similarity Score Calculation:

The similarity score is calculated based on the length of the LCS and the average length of the two documents. This provides a percentage similarity between the two texts.

**Plagiarism Report:**

A detailed report is generated showing the results, including the LCS and similarity score.

**Future Improvements**
Efficiency: Currently, the LCS is computed naively. Optimizations such as Suffix Trees or LCP Arrays can be implemented for better performance, especially for large documents.

Text Preprocessing: The tool can be enhanced to preprocess documents by removing common stop words or normalizing case to improve accuracy in plagiarism detection.

GUI: A graphical user interface (GUI) could be developed to make the tool more user-friendly.

**Acknowledgments**
This project makes use of suffix arrays for efficient string comparison. The concept is derived from string matching algorithms used in text search and bioinformatics.
