# Create the First Page

In this step, you will create the first page of the PDF file. The page will contain a plot of a simple graph.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
