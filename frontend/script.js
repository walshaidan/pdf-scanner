const fileInput = document.getElementById("pdfFile");
const extractButton = document.getElementById("extractButton");
const downloadButton = document.getElementById("downloadButton");

const statusText = document.getElementById("status");
const resultSection = document.getElementById("resultSection");
const resultText = document.getElementById("result");

let extractedText = "";

extractButton.addEventListener("click", async () => {
    const file = fileInput.files[0];
    if (!file) {
        statusText.textContent = "Please select a PDF.";
        return;
    }

    const formData = new FormData();
    // Must match @RequestParam("file")
    formData.append("file", file);
    statusText.textContent = "Extracting text...";

    try {
        const response = await fetch(
            "http://localhost:8080/api/pdf/extract",
            {
                method: "POST",
                body: formData
            }
        );
        if (!response.ok) {
            throw new Error("PDF extraction failed.");
        }

        extractedText = await response.text();
        resultText.value = extractedText;
        resultSection.classList.remove("hidden");
        statusText.textContent = "Extraction complete.";

    } catch (error) {
        console.error(error);
        statusText.textContent =
            "Something went wrong while extracting the PDF.";
    }
});


downloadButton.addEventListener("click", () => {
    const blob = new Blob(
        [extractedText],
        { type: "text/plain" }
    );

    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "extracted.txt";

    link.click();
    URL.revokeObjectURL(url);
});