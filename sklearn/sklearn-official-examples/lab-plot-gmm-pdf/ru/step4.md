# Построение графика оценки плотности

Теперь построим график оценки плотности смеси гауссов. Создадим сетку точек на диапазоне значений датасета и вычислим отрицательный логарифм правдоподобия, предсказанный GMM для каждой точки. Затем отобразим предсказанные оценки в виде контурной диаграммы и рассеянной диаграммы для обучающих данных.

```python
# отображаем предсказанные оценки модели в виде контурной диаграммы
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Density Estimation with Gaussian Mixture Models")
plt.axis("tight")
plt.show()
```
