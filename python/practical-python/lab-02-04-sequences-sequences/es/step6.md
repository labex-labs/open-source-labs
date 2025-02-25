# Declaración break

Puedes usar la declaración `break` para salir de un bucle anticipadamente.

```python
for name in namelist:
    if name == 'Jake':
        break
  ...
  ...
statements
```

Cuando se ejecuta la declaración `break`, sale del bucle y pasa a las siguientes `statements`. La declaración `break` solo se aplica al bucle más interno. Si este bucle está dentro de otro bucle, no romperá el bucle externo.
