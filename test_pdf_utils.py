import pytest

from pdf_utils import *


@pytest.mark.parametrize("input_file, output_file, pages, expected_pages", [
    ("cert.pdf", "output.pdf", "1,10", 10),
    ("cert.pdf", "output.pdf", "-1,0", 0),
])
def test_extract(input_file, output_file, pages, expected_pages):
    extract(input_file, pages)
    reader = PdfReader(output_file)
    num_pages = len(reader.pages)

    assert num_pages == expected_pages

@pytest.mark.parametrize("input_file, n, expected_output_files", [
    ("cert.pdf", 2, ["output1.pdf", "output2.pdf"]),
    ("cert.pdf", 3, ["output1.pdf", "output2.pdf", "output3.pdf"]),
])
def test_split(input_file, n, expected_output_files):
    split(input_file, n)
    assert n == len(expected_output_files)