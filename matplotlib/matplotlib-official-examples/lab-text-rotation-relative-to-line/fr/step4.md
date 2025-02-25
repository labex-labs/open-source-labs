# Tracer du texte sans rotation correcte

Nous allons maintenant tracer du texte aux emplacements spécifiés sans prendre en compte la rotation de la ligne. Cela entraînera que le texte soit tourné à un angle de 45 degrés, ce qui n'est pas ce que nous voulons.

```python
# Tracer du texte
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
