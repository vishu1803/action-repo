#!/usr/bin/env python3
"""
Sample Python script to read a file
"""

# Method 1: Basic file reading with open()
def read_file_basic(filename):
    """Read entire file content"""
    with open(filename, 'r') as file:
        content = file.read()
    return content


# Method 2: Read file line by line
def read_file_lines(filename):
    """Read file line by line"""
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())  # strip() removes trailing newlines
    return lines


# Method 3: Read all lines at once
def read_file_readlines(filename):
    """Read all lines at once"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


# Method 4: Read file with error handling
def read_file_safe(filename):
    """Read file with error handling"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    filename = "README.md"
    
    # Read the file
    content = read_file_safe(filename)
    
    if content:
        print("File content:")
        print(content)
        print("\n" + "="*50 + "\n")
        
        # Read as lines
        lines = read_file_lines(filename)
        print(f"Total lines: {len(lines)}")
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line}")
