# Carregar Dados

Em seguida, carregaremos os dados de amostra que usaremos para este tutorial. Usaremos o arquivo `jacksboro_fault_dem.npz`, que contém dados de elevação.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
