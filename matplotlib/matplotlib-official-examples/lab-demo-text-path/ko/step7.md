# 이미지 표시

다음 코드를 사용하여 최종 이미지를 표시합니다.

```python
ax1.imshow([[0, 1, 2], [1, 2, 3]], cmap=plt.cm.gist_gray_r,
               interpolation="bilinear", aspect="auto")
plt.show()
```
