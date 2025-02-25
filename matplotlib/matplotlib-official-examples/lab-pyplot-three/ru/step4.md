# Добавляем подписи и заголовок

В этом шаге мы добавим заголовок к графику и подписания к осям x и y.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.title("Multiple Datasets")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()
```
