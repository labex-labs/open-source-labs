# Обучение и оценка классификаторов

Мы обучим каждый классификатор на различных пропорциях обучающих данных, от 1% до 95%, и оценим их производительность на тестовом наборе. Этот процесс мы повторим 10 раз, чтобы получить более точную оценку коэффициента ошибки тестирования.

```python
heldout = [0.01, 0.05, 0.25, 0.5, 0.75, 0.9, 0.95]
rounds = 10
xx = 1.0 - np.array(heldout)

for name, clf in classifiers:
    print("Training %s" % name)
    yy = []
    for i in heldout:
        yy_ = []
        for r in range(rounds):
            X_train_, X_test_, y_train_, y_test_ = train_test_split(X_train, y_train, test_size=i, random_state=r)
            clf.fit(X_train_, y_train_)
            y_pred = clf.predict(X_test_)
            yy_.append(1 - np.mean(y_pred == y_test_))
        yy.append(np.mean(yy_))
    plt.plot(xx, yy, label=name)

plt.legend(loc="upper right")
plt.xlabel("Proportion of training data")
plt.ylabel("Test error rate")
plt.show()
```
