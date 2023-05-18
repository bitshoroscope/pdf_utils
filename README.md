# PDF Utilities
This is a Python library that provides utilities for working with PDF files. The library includes functions for extracting pages from a PDF file and splitting a PDF file into multiple parts.

## Installation
To install the library, run the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage
To extract pages from a PDF file, use the extract() function. 
The function takes two arguments: the name of the PDF file and a list of page numbers. The page numbers can be specified as a comma-separated list or as a range. 

### extract  
For example, to extract the first two pages from a PDF file named input.pdf, you would use the following code:

```
python pdf_utils.py cert.pdf extract 1,20
```

### split
To split a PDF file into multiple parts, use the split() function. 
The function takes two arguments: the name of the PDF file and the number of parts to split the file into. 

For example, to split a PDF file named input.pdf into three parts, you would use the following code:

```
python pdf_utils.py cert.pdf split 3 
```


### Happy Splitting
🐍 by @BitsHoroscope