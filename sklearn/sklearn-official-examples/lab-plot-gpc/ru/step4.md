# Построение постериорных распределений

Мы построим постериорные распределения модели GPC с использованием как фиксированных, так и оптимизированных гиперпараметров. Мы построим обучающие данные, тестовые данные и предсказанную вероятность класса 1. Также мы подписываем графики.

```python
# Plot posteriors
plt.figure()
plt.scatter(X[:train_size, 0], y[:train_size], c="k", label="Train data", edgecolors=(0, 0, 0))
plt.scatter(X[train_size:, 0], y[train_size:], c="g", label="Test data", edgecolors=(0, 0, 0))
X_ = np.linspace(0, 5, 100)
plt.plot(X_, gp_fix.predict_proba(X_[:, np.newaxis])[:, 1], "r", label="Initial kernel: %s" % gp_fix.kernel_)
plt.plot(X_, gp_opt.predict_proba(X_[:, np.newaxis])[:, 1], "b", label="Optimized kernel: %s" % gp_opt.kernel_)
plt.xlabel("Feature")
plt.ylabel("Class 1 probability")
plt.xlim(0, 5)
plt.ylim(-0.25, 1.5)
plt.legend(loc="best")
```
