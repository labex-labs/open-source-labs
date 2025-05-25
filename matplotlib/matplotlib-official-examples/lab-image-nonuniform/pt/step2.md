# Criar Arrays Lineares e Não Lineares

Precisamos criar dois arrays, um com valores lineares e outro com valores não lineares. Esses arrays serão usados para criar nosso `NonUniformImage`.

```python
# Array x linear para centros de células:
x = np.linspace(-4, 4, 9)

# Array x altamente não linear:
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
