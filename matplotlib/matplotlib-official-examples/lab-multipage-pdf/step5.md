# Create the Third Page

In this step, you will create the third page of the PDF file. The page will contain a plot of a parabola.

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
plt.close()
```
