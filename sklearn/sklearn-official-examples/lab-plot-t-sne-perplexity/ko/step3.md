# 데이터 시각화

산점도를 사용하여 동심원 데이터셋을 시각화할 수 있습니다.

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(X[red, 0], X[red, 1], c="r")
ax.scatter(X[green, 0], X[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
