from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    """Opens a PDF file and extracts all visible text into a single string."""
    try:
        # Load the PDF file
        reader = PdfReader(pdf_path)
        extracted_text = ""
        
        # Loop through every page and pull the text
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
        
        # Clean up any trailing whitespace
        return extracted_text.strip()
        
    except Exception as e:
        return f"Error reading PDF file: {str(e)}"

# This block allows us to test the file directly from the terminal
if __name__ == "__main__":
    print("Testing PDF Parser...")
    
    # Path to our sample resume in the root folder
    test_pdf = "sample_resume.pdf"
    
    resume_text = extract_text_from_pdf(test_pdf)
    
    # Print the first 300 characters to verify it works without cluttering the screen
    print("\n--- Extracted Text Preview ---")
    print(resume_text[:300] + "...")
    print("------------------------------")
    print(f"Total characters extracted: {len(resume_text)}")
