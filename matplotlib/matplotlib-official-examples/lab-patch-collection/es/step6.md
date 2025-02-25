# Agregar condiciones de límite a los segmentos circulares

Agregamos condiciones de límite a los segmentos circulares.

```python
patches += [
    Wedge((.3,.7),.1, 0, 360),             # Círculo completo
    Wedge((.7,.8),.2, 0, 360, width=0.05),  # Anillo completo
    Wedge((.8,.3),.2, 0, 45),              # Sector completo
    Wedge((.8,.3),.2, 45, 90, width=0.10),  # Sector de anillo
]
```
