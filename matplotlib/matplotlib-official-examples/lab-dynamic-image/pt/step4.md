# Gerar os Dados

Usaremos o método `linspace` da biblioteca Numpy para gerar os dados para a animação. Geraremos dois conjuntos de dados, x e y, e então remodelaremos os dados y para criar um array bidimensional.

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
