import pymupdf
import TableFormatter
import TableDetector

def run_application(pdf,output_path):
    with open(output_path, "w") as file:
        pass

    try:
        document = pymupdf.open(pdf)
        output = open(output_path,"wb")
    except pymupdf.FileNotFoundError:
        print("File Not Found!")
        return
    except pymupdf.FileDataError:
        print("Error Reading/Opening That File")
        return

    for page in document:
        blocks = page.get_text("dict")["blocks"]
        tabs = page.find_tables()
        pageImages = page.get_image_info(False, True)
        xref_no = 0
        next_is_table = False
        i = 0


        for block in blocks:
            if block["type"] == 0:
                if TableDetector.is_table_below(block["bbox"],tabs):
                    next_is_table = True

                if next_is_table:
                    output.write(get_block_text(block).encode("utf8"))
                    TableFormatter.write_table(tabs.tables[i].extract(), output)
                    i += 1
                    next_is_table = False
                else:
                    if TableDetector.is_block_in_table(block["bbox"], tabs.tables):
                        continue
                    output.write(get_block_text(block).encode("utf8"))
            elif block["type"] == 1:
                pixmap = pymupdf.Pixmap(document,pageImages[xref_no]["xref"])
                xref_no += 1

                pdf_bytes = pixmap.pdfocr_tobytes(
                    language="eng",
                    tessdata="/opt/homebrew/share/tessdata"
                )

                ocr_document = pymupdf.open(
                    stream=pdf_bytes,
                    filetype="pdf"
                )

                ocr_page = ocr_document[0]
                output.write(ocr_page.get_text().encode("utf8"))

                ocr_tabs = ocr_page.find_tables(
                    strategy="text"
                )
                for table in ocr_tabs.tables:
                    # TableFormatter.write_table(table.extract(),output)
                    print(table.extract())


        output.write(bytes((12,)))
        output.write(b"\n")

    document.close()
    output.close()

def get_block_text(block):
    text = ""
    for line in block["lines"]:
        for span in line["spans"]:
            text += span["text"]
        text += "\n"

    return text