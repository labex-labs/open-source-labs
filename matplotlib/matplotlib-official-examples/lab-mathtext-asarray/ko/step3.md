# 텍스트 이미지를 figure 에 그리기

텍스트를 RGBA 이미지로 변환했으면, `.Figure.figimage`를 사용하여 figure 에 그릴 수 있습니다.

```python
fig = plt.figure()
rgba1 = text_to_rgba(r"IQ: $\sigma_i=15$", color="blue", fontsize=20, dpi=200)
rgba2 = text_to_rgba(r"some other string", color="red", fontsize=20, dpi=200)

fig.figimage(rgba1, 100, 50)
fig.figimage(rgba2, 100, 150)

plt.show()
```
