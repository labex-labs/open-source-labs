# Tracer du texte avec rotation correcte

Enfin, nous allons tracer du texte aux emplacements spécifiés tout en tenant compte de la rotation de la ligne. Cela entraînera que le texte soit tourné à l'angle correct par rapport à la ligne.

```python
# Tracer du texte
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
