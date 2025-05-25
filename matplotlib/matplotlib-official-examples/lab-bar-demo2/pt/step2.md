# Criar Dados para o Gráfico de Barras

Nesta etapa, precisamos criar dados para o gráfico de barras. Usaremos a biblioteca numpy para criar um array de valores que usaremos para o gráfico de barras.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
