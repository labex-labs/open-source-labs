# Módulos como entornos

Los módulos forman un entorno envolvente para todo el código definido dentro de ellos.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

Las variables _globales_ siempre están vinculadas al módulo envolvente (mismo archivo). Cada archivo fuente es su propio pequeño universo.
