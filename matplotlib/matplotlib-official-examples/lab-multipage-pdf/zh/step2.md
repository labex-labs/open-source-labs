# 创建 PdfPages 对象

接下来，你需要创建一个 PdfPages 对象，用于保存 PDF 文件的各个页面。你可以使用 `with` 语句来确保即使发生异常，PdfPages 对象也会在代码块结束时正确关闭。

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
