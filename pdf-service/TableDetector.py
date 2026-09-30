import pymupdf

def is_table_below(box_bbox, table, max_gap=20):
    box = pymupdf.Rect(box_bbox)

    for tab in table:
        table = pymupdf.Rect(tab.bbox)
        vertical_gap = table.y0 - box.y1
        if 0 <= vertical_gap <= max_gap:
            return True
    return False


def is_block_in_table(block_bbox,tables):
    block = pymupdf.Rect(block_bbox)
    for table in tables:
        table_rect = pymupdf.Rect(table.bbox)
        if block.intersects(table_rect):
            return True
    return False