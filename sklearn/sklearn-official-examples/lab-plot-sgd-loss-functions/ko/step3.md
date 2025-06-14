# 손실 함수 시각화

`matplotlib` 라이브러리를 사용하여 `scikit-learn`에서 지원하는 다양한 볼록 손실 함수를 시각화합니다.

```python
lw = 2
plt.plot([xmin, 0, 0, xmax], [1, 1, 0, 0], color="gold", lw=lw, label="Zero-one loss")
plt.plot(xx, np.where(xx < 1, 1 - xx, 0), color="teal", lw=lw, label="Hinge loss")
plt.plot(xx, -np.minimum(xx, 0), color="yellowgreen", lw=lw, label="Perceptron loss")
plt.plot(xx, np.log2(1 + np.exp(-xx)), color="cornflowerblue", lw=lw, label="Log loss")
plt.plot(xx, np.where(xx < 1, 1 - xx, 0) ** 2, color="orange", lw=lw, label="Squared hinge loss")
plt.plot(xx, modified_huber_loss(xx, 1), color="darkorchid", lw=lw, linestyle="--", label="Modified Huber loss")
plt.ylim((0, 8))
plt.legend(loc="upper right")
plt.xlabel(r"결정 함수 $f(x)$")
plt.ylabel("$L(y=1, f(x))$")
plt.show()
```
