# 두 번째 페이지 생성

이 단계에서는 PDF 파일의 두 번째 페이지를 생성합니다. 이 페이지에는 사인파의 플롯이 포함됩니다.

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
