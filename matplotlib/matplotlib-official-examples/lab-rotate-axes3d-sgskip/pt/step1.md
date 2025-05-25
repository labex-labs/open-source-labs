# Importar Bibliotecas e Conjunto de Dados

Primeiramente, precisamos importar as bibliotecas e o conjunto de dados necessários. Neste exemplo, usaremos as bibliotecas `matplotlib` e `mpl_toolkits.mplot3d` para criar o gráfico 3D, e a função `axes3d.get_test_data()` para gerar um conjunto de dados de exemplo.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
