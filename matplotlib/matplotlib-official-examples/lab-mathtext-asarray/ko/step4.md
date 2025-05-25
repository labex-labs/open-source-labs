# 픽셀 좌표로 figure 에 텍스트 그리기

또는, `.transforms.IdentityTransform`과 함께 `.Figure.text`를 사용하여 픽셀 좌표로 위치를 지정하여 figure 에 직접 텍스트를 그릴 수 있습니다.

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
