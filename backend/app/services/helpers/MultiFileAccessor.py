import pdfplumber
import io
import asyncio

class MultiFileAccessor:
    def __init__(self, files):
        self.files = files or []

    async def convert_to_text(self):
        result = ""
        for index, upload_file in enumerate(self.files, start=1):
            file_name = upload_file.filename  # Get the filename from the UploadFile object
            result += f"File id : {index}\n"
            result += f"CV name : {file_name}\n"
            
            # Read the content of the UploadFile object
            content = await upload_file.read()
            
            # Use io.BytesIO to convert the content to a file-like object
            with pdfplumber.open(io.BytesIO(content)) as pdf:
                text = ""
                # Iterate through each page
                for page in pdf.pages:
                    # Extract text from the page
                    text += page.extract_text() or ""  # Handle cases where extract_text() returns None
                
                result += text + "\n"  # Add the extracted text to the result
        return result
    
if __name__ == '__main__':
    files_path = [
        'D:\\carrier\\project\\parsing-cvs\\backend\\app\\resources\\CVToTest.pdf', 
        'D:\\carrier\\project\\parsing-cvs\\backend\\app\\resources\\CVToTest.pdf'
    ]
    
    multi_file_accessor = MultiFileAccessor(files_path)
    
    # Use asyncio.run to run the coroutine
    result = asyncio.run(multi_file_accessor.convert_to_text())
    print(result)