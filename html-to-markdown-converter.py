import os
from markdownify import markdownify

def convert_html_to_markdown(source_file, target_file):
    """
    Convert an HTML file to a Markdown file using markdownify library.
    
    Args:
        source_file (str): Path to the source HTML file
        target_file (str): Path to the target Markdown file
    
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Check if source file exists
        if not os.path.exists(source_file):
            print(f"Error: Source file '{source_file}' does not exist.")
            return False
            
        # Read HTML content from source file
        with open(source_file, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        
        # Convert HTML to Markdown
        markdown_content = markdownify(html_content, heading_style="ATX")
        
        # Write Markdown content to target file
        with open(target_file, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)
            
        print(f"Successfully converted '{source_file}' to '{target_file}'")
        return True
        
    except Exception as e:
        print(f"Error converting HTML to Markdown: {str(e)}")
        return False

if __name__ == "__main__":
    convert_html_to_markdown("test-data/SHARED-test-short-output.html", "test-data/SHARED-test-short-output.md")
