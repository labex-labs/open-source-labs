# Trazar texto sin la rotación correcta

Ahora trazaremos texto en las ubicaciones especificadas sin tener en cuenta la rotación de la línea. Esto hará que el texto se rote a un ángulo de 45 grados, lo cual no es lo que queremos.

```python
# Trazar texto
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
