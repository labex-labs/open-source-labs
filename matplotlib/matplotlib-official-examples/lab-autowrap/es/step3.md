# Envolver automáticamente el texto

Ahora, exploremos cómo envolver automáticamente el texto en Matplotlib. Reemplace la línea `plt.text()` en su código con la siguiente:

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

El argumento `wrap=True` le dice a Matplotlib que envuelva automáticamente el texto.
