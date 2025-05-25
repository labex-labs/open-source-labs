# Mascarando os Dados

Nesta etapa, mascararemos alguns dos valores `z` usando uma máscara booleana. Criamos um array `mask` usando a função `np.zeros_like()` e, em seguida, definimos alguns dos valores como `True` para mascará-los.

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
