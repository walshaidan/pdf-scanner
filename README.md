# PDF Scanner

PDF Scanner is a full-stack application for extracting text and tables from PDF documents.

The application uses a Java Spring Boot backend as the main API, which sends uploaded PDF files to a Python FastAPI service for processing. The extracted text is then returned to the frontend where it can be viewed and downloaded as a `.txt` file.

## Architecture

```text
Frontend
   |
   | POST PDF
   v
Spring Boot API
localhost:8080
   |
   | multipart/form-data
   v
Python FastAPI Service
localhost:8000
   |
   | PyMuPDF / OCR
   v
PDF Text Extraction
   |
   | text/plain
   v
Spring Boot
   |
   v
Frontend
```

## Technologies

### Frontend

- HTML
- CSS
- JavaScript
- Fetch API

### Backend

- Java 17
- Spring Boot
- Spring MVC
- Spring RestClient
- Maven

### PDF Processing

- Python
- FastAPI
- PyMuPDF
- Tesseract OCR

## Project Structure

```text
pdf-scanner/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend-pdf-scanner/
│   ├── src/
│   ├── pom.xml
│   ├── mvnw
│   └── mvnw.cmd
│
├── pdf-service/
│   ├── main.py
│   ├── PDFExtractor.py
│   ├── TableDetector.py
│   ├── TableFormatter.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

## How It Works

1. The user selects a PDF from the frontend.
2. JavaScript creates a `multipart/form-data` request containing the PDF.
3. The PDF is sent to the Spring Boot API.
4. Spring Boot forwards the PDF to the Python FastAPI service.
5. PyMuPDF extracts text and detects tables.
6. OCR is used where required for image-based content.
7. The extracted text is returned to Spring Boot.
8. Spring Boot returns the result as `text/plain`.
9. The frontend displays the extracted text and allows it to be downloaded as a `.txt` file.

## Requirements

Before running the project, install:

- Java 17
- Python 3
- Tesseract OCR

## Python Setup

Navigate to the Python service:

```bash
cd pdf-service
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

### Tesseract

Tesseract must be installed separately because it is a system dependency.

On macOS with Homebrew:

```bash
brew install tesseract
```

The application uses the `TESSDATA_PATH` environment variable to locate Tesseract language data.

For a typical Homebrew installation on Apple Silicon:

```bash
export TESSDATA_PATH=/opt/homebrew/share/tessdata
```

You can verify the variable with:

```bash
echo $TESSDATA_PATH
```

## Running the Python Service

From `pdf-service/` with the virtual environment activated:

```bash
uvicorn main:app --reload --port 8000
```

The Python API will run at:

```text
http://localhost:8000
```

FastAPI documentation is available at:

```text
http://localhost:8000/docs
```

## Running the Spring Boot Backend

Navigate to:

```bash
cd backend-pdf-scanner
```

On macOS/Linux:

```bash
./mvnw spring-boot:run
```

Alternatively, run the Spring Boot application directly from IntelliJ IDEA.

The backend runs at:

```text
http://localhost:8080
```

The PDF extraction endpoint is:

```text
POST /api/pdf/extract
```

It accepts:

```text
multipart/form-data
```

with a form field named:

```text
file
```

and returns:

```text
text/plain
```

## Running the Frontend

Navigate to:

```bash
cd frontend
```

Start a simple development server:

```bash
python3 -m http.server 5500
```

Then open:

```text
http://localhost:5500
```

## Running the Complete Application

Three processes need to be running during development.

### Terminal 1 — Python

```bash
cd pdf-service
source venv/bin/activate
export TESSDATA_PATH=/opt/homebrew/share/tessdata
uvicorn main:app --reload --port 8000
```

### Terminal 2 — Spring Boot

```bash
cd backend-pdf-scanner
./mvnw spring-boot:run
```

### Terminal 3 — Frontend

```bash
cd frontend
python3 -m http.server 5500
```

Then visit:

```text
http://localhost:5500
```

## API Example

A PDF can also be uploaded directly using `curl`:

```bash
curl -X POST \
  -F "file=@example.pdf" \
  http://localhost:8080/api/pdf/extract
```

## Current Features

- PDF file upload
- Text extraction
- Multi-page PDF processing
- Unicode character extraction
- Table detection and formatting
- OCR support for image-based content
- Extracted text preview
- `.txt` file download
- Spring Boot to Python service communication

## Future Improvements

Potential improvements include:

- Improved error handling
- PDF file validation
- Improved OCR table extraction
- Automated tests
- Docker support
- Configurable service URLs
- Improved frontend loading and error states
- Deployment configuration

## Author

Aidan Walsh