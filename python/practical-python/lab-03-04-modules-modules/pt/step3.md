# Definições Globais

Tudo o que é definido no escopo _global_ é o que preenche o namespace (espaço de nomes) do módulo. Considere dois módulos que definem a mesma variável `x`.

```python
# foo.py
x = 42
def grok(a):
    ...
```

```python
# bar.py
x = 37
def spam(a):
    ...
```

Neste caso, as definições de `x` referem-se a variáveis diferentes. Uma é `foo.x` e a outra é `bar.x`. Módulos diferentes podem usar os mesmos nomes e esses nomes não entrarão em conflito entre si.

**Módulos são isolados.**
