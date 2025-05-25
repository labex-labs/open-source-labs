# Criar os dados

Nesta etapa, criamos os dados que usaremos para criar nosso gráfico de barras de erro.

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```
