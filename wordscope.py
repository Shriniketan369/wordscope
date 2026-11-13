import sys
from collections import Counter

STOP_WORDS = {
    "the", "and", "to", "it", "a", "on", "of", "in", "is", "for",
    "that", "this", "with", "as", "are", "be", "by", "or", "an", "at",
}

def count_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()

    # Keep only letters and spaces
    cleaned = "".join(ch if ch.isalpha() or ch.isspace() else " " for ch in text)
    words = cleaned.split()

    # Remove common filler words
    words = [w for w in words if w not in STOP_WORDS]

    return Counter(words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wordscope.py <filename> [top_n]")
        sys.exit(1)

    filename = sys.argv[1]
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    counts = count_words(filename)

    print(f"Total words (after filtering): {sum(counts.values())}")
    print(f"Unique words: {len(counts)}")
    print(f"Top {top_n} words:")
    for word, n in counts.most_common(top_n):
        print(f"  {word}: {n}")
