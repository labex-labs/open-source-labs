# Carregar os dados

Em seguida, carregaremos os dados que queremos plotar. Usaremos um array de registro numpy a partir de dados CSV do Yahoo com os campos date, open, high, low, close, volume, adj_close do diretório mpl-data/sample_data. O array de registro armazena a data como um np.datetime64 com uma unidade de dia ('D') na coluna de data.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
