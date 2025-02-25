# Trazar texto con la rotación correcta

Finalmente, trazaremos texto en las ubicaciones especificadas teniendo en cuenta la rotación de la línea. Esto hará que el texto se rote al ángulo correcto con respecto a la línea.

```python
# Trazar texto
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
