import mammoth

def convert_docx_to_html(source_filename, target_filename):
    """
    Convert a DOCX file to HTML using the mammoth library.
    
    Args:
        source_filename (str): Path to the source DOCX file
        target_filename (str): Path to the target HTML file
    
    Returns:
        dict: Result containing success status and any messages/warnings
    """
    try:
        with open(source_filename, "rb") as docx_file:
            # Convert the document
            result = mammoth.convert_to_html(docx_file)
            html = result.value
            
            # Write the HTML to the target file
            with open(target_filename, "w", encoding="utf-8") as html_file:
                html_file.write(html)
            
            # Return the result including any warnings
            return {
                "success": True,
                "messages": result.messages,
                "html": html
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    result = convert_docx_to_html("test-data/SHARED-test-short-output.docx", "test-data/SHARED-test-short-output.html")
    if result["success"]:
        print(f"Conversion successful.")
        if result["messages"]:
            print(f"Warnings: {result['messages']}")
    else:
        print(f"Conversion failed: {result['error']}")