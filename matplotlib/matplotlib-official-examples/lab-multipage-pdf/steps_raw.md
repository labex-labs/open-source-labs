# Creating a Multipage PDF with Python Matplotlib

## Introduction

In this lab, you will learn how to create a multipage PDF file with Python Matplotlib. The PDF file will contain several pages with different plots and metadata. You will also learn how to attach annotations to the PDF file.

## Steps

### Step 1: Import Libraries

First, you need to import the necessary libraries for creating the PDF file. In this lab, we will use Matplotlib and datetime libraries.

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
```

### Step 2: Create the PdfPages Object

Next, you need to create a PdfPages object to which you will save the pages of the PDF file. You can use the 'with' statement to make sure that the PdfPages object is closed properly at the end of the block, even if an exception occurs.

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```

### Step 3: Create the First Page

In this step, you will create the first page of the PDF file. The page will contain a plot of a simple graph.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```

### Step 4: Create the Second Page

In this step, you will create the second page of the PDF file. The page will contain a plot of a sine wave.

```python
plt.rcParams['text.usetex'] = True
plt.figure(figsize=(8, 6))
x = np.arange(0, 5, 0.1)
plt.plot(x, np.sin(x), 'b-')
plt.title('Page Two')
pdf.attach_note("plot of sin(x)")  # attach metadata (as pdf note) to page
pdf.savefig()
plt.close()
```

### Step 5: Create the Third Page

In this step, you will create the third page of the PDF file. The page will contain a plot of a parabola.

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
plt.close()
```

### Step 6: Set the Metadata of the PDF File

In this step, you will set the metadata of the PDF file. You can set the title, author, subject, keywords, and creation/modification date of the PDF file.

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```

## Summary

In this lab, you learned how to create a multipage PDF file with Python Matplotlib. You also learned how to attach metadata and annotations to the PDF file. You can use these techniques to create professional reports with multiple plots and annotations.
