# Configurez les vecteurs et les matrices d'enquête

Ensuite, configurez les vecteurs et les matrices d'enquête. Conceptez la charge surfacique et le rapport d'engrenage.

```python
nx = 101
ny = 105

# Configurez les vecteurs d'enquête
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# Configurez les matrices d'enquête.  Conceptez la charge surfacique et le rapport d'engrenage.
x1, x2 = np.meshgrid(xvec, yvec)
```
