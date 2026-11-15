# DAA Mini Project: Naive and Rabin-Karp String Matching
# Aim: Implement and compare two string matching algorithms.

import time


def naive_search(text, pattern):
    """Return all starting indices where pattern occurs in text."""
    positions = []
    n, m = len(text), len(pattern)

    if m == 0 or m > n:
        return positions

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i)

    return positions


def rabin_karp_search(text, pattern, prime=101, base=256):
    """Return all matches using a rolling hash."""
    positions = []
    n, m = len(text), len(pattern)

    if m == 0 or m > n:
        return positions

    high_order = pow(base, m - 1, prime)
    pattern_hash = 0
    window_hash = 0

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        # Verify characters after a hash match to avoid false positives.
        if pattern_hash == window_hash and text[i:i + m] == pattern:
            positions.append(i)

        if i < n - m:
            window_hash = (
                base * (window_hash - ord(text[i]) * high_order)
                + ord(text[i + m])
            ) % prime

    return positions


def main():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")

    start = time.perf_counter()
    naive_positions = naive_search(text, pattern)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    rk_positions = rabin_karp_search(text, pattern)
    rk_time = time.perf_counter() - start

    print("\nNaive String Matching")
    print("Pattern positions (0-based):", naive_positions)
    print("Number of matches:", len(naive_positions))
    print(f"Execution time: {naive_time:.8f} seconds")

    print("\nRabin-Karp String Matching")
    print("Pattern positions (0-based):", rk_positions)
    print("Number of matches:", len(rk_positions))
    print(f"Execution time: {rk_time:.8f} seconds")

    print("\nResults match:", naive_positions == rk_positions)
    print("Naive worst-case time complexity: O(n*m)")
    print("Rabin-Karp average time complexity: O(n + m)")
    print("Rabin-Karp worst-case time complexity: O(n*m)")
    print("Auxiliary space: O(1), excluding stored match positions")


if __name__ == "__main__":
    main()
