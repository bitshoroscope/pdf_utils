import argparse
from PyPDF2 import PdfReader, PdfWriter

writer = PdfWriter()

def extract(file_name, pages):
    """Extracts the specified pages from the PDF file."""
    reader = PdfReader(file_name)
    writer = PdfWriter()

    start, ending = map(int, pages.split(","))
    page_range = range(start, ending + 1)

    for page_num, page in enumerate(reader.pages, 1):
        if page_num in page_range:
            writer.add_page(page)

    with open(f'output.pdf', 'wb') as out:
        writer.write(out)


def split(file_name, n):
    """Splits the PDF file into n equal parts. If the last árt is shorter it will consider it."""
    reader = PdfReader(file_name)
    num_pages = len(reader.pages)

    page_size = (num_pages // n) + 1
    cursor = 0

    for i in range(n):
        writer = PdfWriter()
        for j in range(page_size):
            if cursor == num_pages:
                break
            writer.add_page(reader.pages[j + i * page_size])
            cursor = cursor + 1

        with open(f'output{i + 1}.pdf', 'wb') as out:
            writer.write(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="The name of the PDF file")
    parser.add_argument("action", help="The action to perform")
    parser.add_argument("args", help="The arguments for the action")

    args = parser.parse_args()

    if args.action == "extract":
        extract(args.file_name, args.args)
    elif args.action == "split":
        split(args.file_name, int(args.args))
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()