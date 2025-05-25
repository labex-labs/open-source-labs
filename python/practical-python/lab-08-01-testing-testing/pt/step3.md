# Testes Inline (Inline Tests)

As asserções também podem ser usadas para testes simples.

```python
def add(x, y):
    return x + y

assert add(2,2) == 4
```

Dessa forma, você está incluindo o teste no mesmo módulo que seu código.

_Benefício: Se o código estiver obviamente quebrado, as tentativas de importar o módulo irão travar._

Isso não é recomendado para testes exaustivos. É mais um "teste superficial" básico. A função funciona em algum exemplo? Se não, então algo está definitivamente quebrado.
