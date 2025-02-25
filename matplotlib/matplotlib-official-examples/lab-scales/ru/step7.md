# Создаем график с масштабом преобразования Меркатора

В качестве бонусного материала мы также создадим график, используя функцию преобразования Меркатора. Это не встроенная функция в Matplotlib, но мы можем определить собственные функции прямого и обратного преобразования, чтобы создать график с масштабом преобразования Меркатора. В этом примере мы определим функции `forward()` и `inverse()` для преобразования Меркатора. Также добавим заголовок и сетку к графику.

```python
# Функция преобразования Меркатора
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
