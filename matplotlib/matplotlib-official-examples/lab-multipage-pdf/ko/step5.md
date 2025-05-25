# 세 번째 페이지 생성

이 단계에서는 PDF 파일의 세 번째 페이지를 생성합니다. 이 페이지에는 포물선의 플롯이 포함됩니다.

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
plt.close()
```
