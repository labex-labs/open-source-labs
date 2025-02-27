# Строим контур

Мы строим контур функции принятия решений. Сначала мы создаем сетку точек с использованием массивов `xx` и `yy`. Затем мы преобразуем сетку точек в двумерный массив и применяем метод `decision_function` класса `SVC`, чтобы получить предсказанные значения. Затем мы строим контур с использованием метода `contourf`.

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```
