# Ajoutez des conditions limites aux segments circulaires

Nous ajoutons des conditions limites aux segments circulaires.

```python
patches += [
    Wedge((.3,.7),.1, 0, 360),             # Cercle complet
    Wedge((.7,.8),.2, 0, 360, width=0.05),  # Bague complète
    Wedge((.8,.3),.2, 0, 45),              # Secteur complet
    Wedge((.8,.3),.2, 45, 90, width=0.10),  # Secteur de bague
]
```
