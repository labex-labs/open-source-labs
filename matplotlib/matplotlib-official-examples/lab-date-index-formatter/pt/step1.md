# Importar Bibliotecas e Dados Necessários

Primeiramente, precisamos importar as bibliotecas necessárias, que são `matplotlib`, `numpy` e `matplotlib.cbook`. Também precisamos carregar um array de registro numpy a partir de dados CSV do Yahoo com os campos date (data), open (abertura), high (máxima), low (mínima), close (fechamento), volume, adj_close (fechamento ajustado) do diretório mpl-data/sample_data. O array de registro armazena a data como um `np.datetime64` com uma unidade de dia ('D') na coluna de data. Usaremos esses dados para plotar a série temporal financeira.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load data from sample_data directory
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # get the first 9 days
```
