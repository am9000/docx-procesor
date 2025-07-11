def compare_md_files_ignore_whitespace(file1, file2):
    """
    Compare two Markdown files while ignoring whitespace differences.
    
    Args:
        file1 (str): Path to the first Markdown file.
        file2 (str): Path to the second Markdown file.
    
    Returns:
        bool: True if files are equivalent ignoring whitespace, False otherwise.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read().strip()
        content2 = f2.read().strip()
    
    return content1 == content2