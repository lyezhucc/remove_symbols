import sys
import os

def remove_symbols_from_file(file_path):
    """
    Removes '##', '###', '**', '————', and '---' from a file.

    Args:
        file_path (str): The path to the file to be processed.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('##', '')
        content = content.replace('###', '')
        content = content.replace('**', '')
        content = content.replace('————', '')
        content = content.replace('---', '')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Successfully processed file: {file_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_symbols.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    remove_symbols_from_file(file_path)
