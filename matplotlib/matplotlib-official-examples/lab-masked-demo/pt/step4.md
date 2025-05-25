# Mascar Pontos

Mascaremos os pontos onde y > 0.7 usando um array mascarado (masked array). Criaremos um novo array y com valores mascarados.

```python
y3 = np.ma.masked_where(y > 0.7, y)
```
