# 첫 번째 페이지 생성

이 단계에서는 PDF 파일의 첫 번째 페이지를 생성합니다. 이 페이지에는 간단한 그래프의 플롯이 포함됩니다.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
