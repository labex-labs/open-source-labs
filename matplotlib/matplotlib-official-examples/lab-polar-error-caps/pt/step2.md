# Criar Dados

Nesta etapa, criaremos os dados para o nosso gráfico de barras de erro. Usaremos NumPy para criar um array de valores theta e um array de valores de raio correspondentes.

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
