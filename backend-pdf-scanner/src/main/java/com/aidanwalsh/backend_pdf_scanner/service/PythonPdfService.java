package com.aidanwalsh.backend_pdf_scanner.service;

import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestClient;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@Service
public class PythonPdfService {
    private final RestClient restClient;

    public PythonPdfService() {
        this.restClient = RestClient.builder()
                .baseUrl("http://localhost:8000")
                .build();
    }

    public byte[] extractPdf(MultipartFile pdf) throws IOException {
        ByteArrayResource pdfResource = new ByteArrayResource(pdf.getBytes()) {
            @Override
            public String getFilename() {
                return pdf.getOriginalFilename();
            }
        };

        MultiValueMap<String,Object> body = new LinkedMultiValueMap<>();
        body.add("file",pdfResource);

        return restClient.post()
                .uri("/extract")
                .contentType(MediaType.MULTIPART_FORM_DATA)
                .body(body)
                .retrieve()
                .body(byte[].class);
    }
}