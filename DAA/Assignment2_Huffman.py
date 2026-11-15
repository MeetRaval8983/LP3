
# Assignment No. 2: Huffman Encoding Using Greedy Strategy
# Aim: To implement Huffman Encoding and analyze its
# time and space complexity.

import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Compare nodes by frequency for the min heap
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    min_heap = []

    for char, freq in frequency.items():
        heapq.heappush(min_heap, Node(char, freq))

    # Handle empty input
    if not min_heap:
        return None

    # Handle a single unique character
    if len(min_heap) == 1:
        only_node = min_heap[0]
        root = Node(None, only_node.freq)
        root.left = only_node
        return root

    # Greedy strategy: repeatedly combine two minimum frequencies
    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(min_heap, merged)

    return min_heap[0]


def generate_codes(root, code="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = code if code else "0"
        return codes

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)

    return codes


def main():
    text = input("Enter the message: ")

    if not text:
        print("Please enter a non-empty message.")
        return

    frequency = Counter(text)
    root = build_huffman_tree(text)
    codes = generate_codes(root)

    print("\nCharacter Frequencies and Huffman Codes:")
    print("Character\tFrequency\tCode")

    for char, freq in sorted(frequency.items()):
        display_char = repr(char)
        print(f"{display_char}\t\t{freq}\t\t{codes[char]}")

    encoded_message = "".join(codes[char] for char in text)

    print("\nOriginal message:", text)
    print("Encoded message:", encoded_message)
    print("Original size (8-bit characters):", len(text) * 8, "bits")
    print("Encoded size:", len(encoded_message), "bits")

    print("\nTime Complexity: O(n + k log k)")
    print("Space Complexity: O(k) for the tree and codes,")
    print("where n = message length and k = unique characters.")


if __name__ == "__main__":
    main()
