# Генерация данных

Далее мы сгенерируем некоторые фейковые данные для использования в нашем графике. Мы создадим два массива, `a` и `b`, с использованием функции `arange` из NumPy. Затем мы вычислим еще два массива, `c` и `d`, используя функцию `exp` для вычисления экспоненты от `a`, а `d` будет обратным порядком элементов массива `c`.

```python
# Make some fake data.
a = b = np.arange(0, 3,.02)
c = np.exp(a)
d = c[::-1]
```
