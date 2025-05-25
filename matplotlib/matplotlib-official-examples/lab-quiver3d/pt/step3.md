# Definir a Direção das Setas

Agora, definiremos a direção das setas. Neste exemplo, definiremos a direção das setas usando as funções trigonométricas do NumPy. As funções `sin` e `cos` são usadas para criar os arrays `u`, `v` e `w` que representam a direção das setas nas direções `x`, `y` e `z`.

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
