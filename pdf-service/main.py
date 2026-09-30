import os
import tempfile
import PDFExtractor
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PDF service is running"}

@app.post("/extract")
async def extract_pdf(file: UploadFile = File(...)):

    #Only Accept PDFs
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="File must be a PDF"
        )

    # Create temporary PDF
    with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
    ) as temp_pdf:
        temp_pdf.write(await file.read())
        pdf_path = temp_pdf.name

    # Create temporary TXT path
    txt_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".txt"
    )
    txt_path = txt_file.name
    txt_file.close()

    # Run your existing PDF extractor
    PDFExtractor.run_application(
        pdf_path,
        txt_path
    )
    return FileResponse(
        path=txt_path,
        media_type="text/plain",
        filename="output.txt"
    )