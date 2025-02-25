# Отображение числа в диапазон

Напишите функцию под названием `num_to_range`, которая принимает пять аргументов: `num`, `inMin`, `inMax`, `outMin` и `outMax`. Функция должна возвращать `num`, отображенное между `outMin` - `outMax` из `inMin` - `inMax`. Другими словами, функция должна принимать число (`num`), которое попадает в определенный диапазон (`inMin` - `inMax`), и отображать его в новый диапазон (`outMin` - `outMax`).

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
