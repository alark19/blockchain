import hashlib


def compute_sha256(data: str) -> str:
    """Return the SHA-256 hex digest of the given string."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode("utf-8"))
    return sha256_hash.hexdigest()


def count_bit_difference(hash1: str, hash2: str) -> int:
    """Count how many bits differ between two equal-length hex digests."""
    bin1 = bin(int(hash1, 16))[2:].zfill(len(hash1) * 4)
    bin2 = bin(int(hash2, 16))[2:].zfill(len(hash2) * 4)
    return sum(b1 != b2 for b1, b2 in zip(bin1, bin2))


def demonstrate_avalanche_effect(original: str, modified: str) -> None:
    """Print the hashes of two similar inputs and compare them."""
    hash1 = compute_sha256(original)
    hash2 = compute_sha256(modified)

    print(f"Input 1        : {original!r}")
    print(f"SHA-256 Hash 1 : {hash1}")
    print()
    print(f"Input 2        : {modified!r}")
    print(f"SHA-256 Hash 2 : {hash2}")
    print()

    total_bits = len(hash1) * 4
    diff_bits = count_bit_difference(hash1, hash2)
    percent_diff = (diff_bits / total_bits) * 100

    print(f"Number of differing bits : {diff_bits} out of {total_bits}")
    print(f"Percentage difference    : {percent_diff:.2f}%")
    print("-" * 60)


def main():
    print("=" * 60)
    print("SHA-256 HASHING DEMONSTRATION")
    print("=" * 60)

    # 1. Basic hashing of a few sample strings
    sample_inputs = [
        "Hello, World!",
        "RIT Sangli",
        "Password123",
        "",  # empty string
    ]

    print("\n--- Basic SHA-256 Hashes ---\n")
    for text in sample_inputs:
        print(f"Input : {text!r}")
        print(f"Hash  : {compute_sha256(text)}")
        print()

    # 2. Avalanche effect: change a single character
    print("\n--- Avalanche Effect: Single Character Change ---\n")
    demonstrate_avalanche_effect("Hello, World!", "Hello, World?")

    # 3. Avalanche effect: change case of one letter
    print("\n--- Avalanche Effect: Case Change ---\n")
    demonstrate_avalanche_effect("password", "Password")

    # 4. Avalanche effect: add a trailing space
    print("\n--- Avalanche Effect: Trailing Whitespace ---\n")
    demonstrate_avalanche_effect("RIT Sangli", "RIT Sangli ")

    # 5. Interactive mode (loops until you press Enter on an empty line)
    print("\n--- Try Your Own Input ---")
    print("Type a string and press Enter to see its hash.")
    print("Press Enter on an empty line to quit.\n")
    while True:
        user_text = input("Enter a string to hash: ")
        if not user_text:
            print("Exiting. Goodbye!")
            break
        print(f"SHA-256 Hash: {compute_sha256(user_text)}\n")


if __name__ == "__main__":
    main()
