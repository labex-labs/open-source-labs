# 가중치 시각화

마지막으로, MLP 의 첫 번째 층의 가중치를 시각화합니다. 4x4 그리드의 서브플롯을 생성하고 각 가중치를 28x28 픽셀의 회색조 이미지로 표시합니다.

```python
fig, axes = plt.subplots(4, 4)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```
