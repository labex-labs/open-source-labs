# Adicionar Eixos à Figura

Adicionaremos os eixos à figura usando a função `add_axes()` e passando a posição do objeto `Divider`.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
