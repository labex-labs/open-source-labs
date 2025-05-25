# Passando Tuplas e Dicionários

Tuplas podem ser expandidas em argumentos variáveis.

```python
numbers = (2,3,4)
f(1, *numbers)      # Same as f(1,2,3,4)
```

Dicionários também podem ser expandidos em argumentos de palavra-chave.

```python
options = {
    'color' : 'red',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# Same as f(data, color='red', delimiter=',', width=400)
```
