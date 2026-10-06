from pathlib import Path


def extract_text_from_file(file_path):
    """
    Read text from a job-description file.

    Args:
        file_path (str): Path to the JD text file.

    Returns:
        str: Job-description text.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Currently only .txt job-description files are supported.")

    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    print("Job description parser module loaded successfully.")