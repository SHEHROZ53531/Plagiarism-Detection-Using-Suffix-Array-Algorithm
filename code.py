import os

def build_suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

def longest_common_substring(s, sa, doc_split_idx):
    max_len = 0
    lcs_set = set()

    for i in range(1, len(sa)):
        i1, i2 = sa[i-1], sa[i]
        # Check if suffixes are from different documents
        if (i1 < doc_split_idx) != (i2 < doc_split_idx):
            # Compute LCP (naive)
            lcp_len = 0
            while i1 + lcp_len < len(s) and i2 + lcp_len < len(s) and s[i1 + lcp_len] == s[i2 + lcp_len]:
                lcp_len += 1
            if lcp_len > max_len:
                max_len = lcp_len
                lcs_set = {s[i1:i1 + lcp_len]}
            elif lcp_len == max_len and lcp_len > 0:
                lcs_set.add(s[i1:i1 + lcp_len])
    return max_len, lcs_set

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def similarity_score(lcs_length, doc1_len, doc2_len):
    avg_len = (doc1_len + doc2_len) / 2
    return (lcs_length / avg_len) * 100 if avg_len else 0

def main(doc1_path, doc2_path):
    doc1 = read_file(doc1_path)
    doc2 = read_file(doc2_path)

    separator = '#'
    while separator in doc1 or separator in doc2:
        separator += '#'

    combined = doc1 + separator + doc2
    split_idx = len(doc1)

    suffix_array = build_suffix_array(combined)
    lcs_len, lcs_set = longest_common_substring(combined, suffix_array, split_idx)

    score = similarity_score(lcs_len, len(doc1), len(doc2))

    print("\n========================== Plagiarism Checker ==========================")
    print(f"Longest common substring length: {lcs_len}")
    print("Common substrings:")
    for s in lcs_set:
        print(f"- {s!r}")
    print(f"\nSimilarity score: {score:.2f}%")


if __name__ == "__main__":
    # Replace these with actual file paths
    doc1_path = "doc1.txt"
    doc2_path = "doc2.txt"

    if os.path.exists(doc1_path) and os.path.exists(doc2_path):
        main(doc1_path, doc2_path)
    else:
        print("Error: One or both files not found.")
