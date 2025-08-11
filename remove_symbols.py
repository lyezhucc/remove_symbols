import sys
import os
import re

def remove_symbols_from_file(file_path):
    """
    Removes '##', '###', '**' symbols, and lines containing only '————' or '---'.

    Args:
        file_path (str): The path to the file to be processed.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # For inline symbols, simple replace is fine
        content = content.replace('##', '')
        content = content.replace('###', '')
        content = content.replace('**', '')

        # For line-based symbols, use regex to remove the whole line
        content = re.sub(r'^\s*(?:---|————)\s*$\n?', '', content, flags=re.MULTILINE)

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
