# Definindo o JoinStyle

Podemos definir o `JoinStyle` da linha usando o método `set_solid_joinstyle()` do objeto `Line2D`. Criaremos um novo objeto de linha e definiremos seu estilo de junção (join style) como `JoinStyle.bevel`.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
