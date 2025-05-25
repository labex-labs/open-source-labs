# t-SNE 결과 시각화

마지막으로, 산점도를 사용하여 t-SNE 결과를 시각화할 수 있습니다.

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(Y[red, 0], Y[red, 1], c="r")
ax.scatter(Y[green, 0], Y[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
