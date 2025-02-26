# Enfoque un poco mejor

Si vas a capturar todos los errores, este es un enfoque más razonable.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
```

Reporta una razón específica de falla. Casi siempre es una buena idea tener algún mecanismo para ver/reportar errores cuando escribes código que captura todas las posibles excepciones.

En general, sin embargo, es mejor capturar el error tan específicamente como sea razonable. Solo captura los errores que puedas realmente manejar. Deja que otros errores pasen - quizás algún otro código los pueda manejar.
