# Create the PdfPages Object

Next, you need to create a PdfPages object to which you will save the pages of the PDF file. You can use the 'with' statement to make sure that the PdfPages object is closed properly at the end of the block, even if an exception occurs.

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
