# Carregar dados

Carregaremos um array de registro (record array) numpy a partir de dados CSV do Yahoo com os campos date, open, high, low, close, volume, adj_close do diretório mpl-data/sample_data. O array de registro armazena a data como um np.datetime64 com uma unidade de dia ('D') na coluna date.

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days
```
