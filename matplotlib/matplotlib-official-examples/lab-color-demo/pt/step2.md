# Definir os Dados

Em seguida, precisamos definir os dados que usaremos para nosso gráfico. Criaremos uma onda senoidal com 201 pontos de dados:

```python
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)
```
