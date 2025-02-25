# Régler le zoom et l'angle de vue

Réglez le zoom et l'angle de vue en utilisant les méthodes `view_init` et `set_box_aspect`. Nous définirons l'angle de vue à 40 degrés dans la direction X et -30 degrés dans la direction Y, et le zoom à 0,9.

```python
# Régler le zoom et l'angle de vue
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
