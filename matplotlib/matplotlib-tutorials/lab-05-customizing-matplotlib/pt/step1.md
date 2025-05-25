# Definindo rcParams em tempo de execução

Você pode alterar dinamicamente as configurações de configuração padrão em tempo de execução em um script Python ou interativamente a partir do shell Python. A variável `matplotlib.rcParams` é global para o pacote Matplotlib e armazena todas as configurações rc. Para personalizar `rcParams` em tempo de execução, você pode modificá-la diretamente usando o dicionário `mpl.rcParams`. Aqui está um exemplo:

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

Este código altera a largura e o estilo de linha padrão para todos os gráficos criados com Matplotlib.

Vamos ver alguns dados aleatórios plotados com as novas configurações padrão.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
