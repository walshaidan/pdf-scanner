package com.aidanwalsh.backend_pdf_scanner.Controller;

import com.aidanwalsh.backend_pdf_scanner.service.PythonPdfService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.bind.annotation.CrossOrigin;

import java.io.IOException;

@CrossOrigin(origins = "http://localhost:5500")
@RestController
@RequestMapping("/api/pdf")
public class PDFRestController {
    private final PythonPdfService pythonPdfService;

    public PDFRestController(PythonPdfService pythonPdfService) {
        this.pythonPdfService = pythonPdfService;
    }

    @PostMapping(
            value = "/extract",
            consumes = MediaType.MULTIPART_FORM_DATA_VALUE,
            produces = MediaType.TEXT_PLAIN_VALUE
    )
    public ResponseEntity<byte[]> extractPdf(@RequestParam("file") MultipartFile file) throws IOException {
        byte[] result = pythonPdfService.extractPdf(file);
        return ResponseEntity.ok()
                .contentType(MediaType.TEXT_PLAIN)
                .header(
                        HttpHeaders.CONTENT_DISPOSITION,
                        "attachment; filename=\"extracted.txt\""
                )
                .body(result);
    }
}