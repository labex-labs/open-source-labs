# Übergabe von Tupeln und Wörterbüchern

Tupel können in variable Argumente erweitert werden.

```python
numbers = (2,3,4)
f(1, *numbers)      # Entspricht f(1,2,3,4)
```

Wörterbücher können auch in Schlüsselwortargumente erweitert werden.

```python
options = {
    'color' : 'rot',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# Entspricht f(data, color='rot', delimiter=',', width=400)
```
