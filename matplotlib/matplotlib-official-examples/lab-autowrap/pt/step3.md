# Quebrando Texto Automaticamente

Agora, vamos explorar como quebrar texto automaticamente no Matplotlib. Substitua a linha `plt.text()` em seu código pelo seguinte:

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

O argumento `wrap=True` informa ao Matplotlib para quebrar o texto automaticamente.
