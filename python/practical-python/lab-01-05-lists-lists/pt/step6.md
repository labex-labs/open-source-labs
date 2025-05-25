# Listas e Matemática

_Atenção: Listas não foram projetadas para operações matemáticas._

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

Especificamente, listas não representam vetores/matrizes como em MATLAB, Octave, R, etc. No entanto, existem alguns pacotes para ajudá-lo com isso (por exemplo, [numpy](https://numpy.org)).

Neste exercício, experimentamos com o tipo de dado lista do Python. Na última seção, você trabalhou com strings contendo símbolos de ações.

```python
>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
```

Divida-o em uma lista de nomes usando a operação `split()` de strings:

```python
>>> symlist = symbols.split(',')
```
