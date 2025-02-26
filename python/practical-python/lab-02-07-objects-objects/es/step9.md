# Comprobación de tipos

Cómo saber si un objeto es de un tipo específico.

```python
if isinstance(a, list):
    print('a es una lista')
```

Comprobar si es uno de muchos tipos posibles.

```python
if isinstance(a, (list,tuple)):
    print('a es una lista o una tupla')
```

\*Precaución: No excedas en la comprobación de tipos. Puede llevar a una complejidad excesiva de código. Por lo general, solo la harías si al hacerlo se evitaran errores comunes cometidos por otros al usar tu código.
