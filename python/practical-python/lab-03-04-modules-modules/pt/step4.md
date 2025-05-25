# Módulos como Ambientes

Módulos formam um ambiente envolvente para todo o código definido dentro.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

Variáveis _globais_ estão sempre ligadas ao módulo envolvente (mesmo arquivo). Cada arquivo fonte é seu próprio pequeno universo.
