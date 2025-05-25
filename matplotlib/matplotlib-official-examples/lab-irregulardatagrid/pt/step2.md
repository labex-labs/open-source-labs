# Gerar dados aleatórios

Geramos dados aleatórios usando o método `np.random.uniform` do NumPy. Geramos `npts = 200` pontos de dados com valores x e y entre -2 e 2. Também calculamos os valores z usando a função `z = x * np.exp(-x**2 - y**2)`.

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
