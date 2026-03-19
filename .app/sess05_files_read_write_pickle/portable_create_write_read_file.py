# Python script that demonstrates how to create, write and read
# from files using pathlib for OS portability

from pathlib import Path

def create_file(path: Path, content: str):
    """
    Creates a file at the given path and writes the specified content to it.

    :param path (Path): The path of the file to be created.
    :param content (str): The content to be written to the file.
    """
    # Ensure the parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write content with utf-8 encoding
    try:
        with path.open('w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ File created and contents written to:\n{path}')
    except Exception as e:
        print(f'❌ Failed to write to file: {e}')


def read_file(path: Path):
    """
    Reads and prints the contents of the specified file.

    :param path (Path): The path of the file to be read.
    """
    try:
        with path.open('r', encoding='utf-8') as f:
            content = f.read()
        print("\n📄 File contents:")
        print(content)
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"❌ Error reading file: {e}")


# Get the current working directory
current_dir = Path.cwd()
print(f'Current working directory is:\n{current_dir}')

# Get the path to the 'files' directory (one level up)
file_directory = current_dir.parent / 'files'
print(f"The path to the 'files' directory is:\n{file_directory}")

# Set the full path to the file
file_path = file_directory / 'hello_os_portable.txt'
print(f"The full path to the file is:\n{file_path}")

# Content with emoji
content = "Hello 👋👋 from files in Python!!!\n"

# Create the file
create_file(file_path, content)

# Read the file
read_file(file_path)