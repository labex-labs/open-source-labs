# Carregar os Dados

Em seguida, carregamos os dados de elevação de amostra usando a função `get_sample_data` do Matplotlib. Em seguida, extraímos os dados de elevação e o tamanho da célula da grade.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
