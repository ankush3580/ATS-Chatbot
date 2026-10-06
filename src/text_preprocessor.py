import re


def clean_text(text):
    """
    Clean and normalize extracted resume or job-description text.

    Args:
        text (str): Raw text.

    Returns:
        str: Cleaned text.
    """

    # Convert text to lowercase
    text = text.lower()

    # Replace common separators with spaces
    text = re.sub(r"[/|,;:()\[\]{}]", " ", text)

    # Keep letters, numbers, +, #, and .
    # This helps preserve technical terms such as C++, C#, and .NET.
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def tokenize_text(text):
    """
    Convert cleaned text into individual tokens.

    Args:
        text (str): Cleaned text.

    Returns:
        list: List of tokens.
    """

    return text.split()


if __name__ == "__main__":
    sample_text = "Python, Machine Learning, C++ and SQL!"

    cleaned = clean_text(sample_text)
    tokens = tokenize_text(cleaned)

    print("Cleaned text:")
    print(cleaned)

    print("\nTokens:")
    print(tokens)