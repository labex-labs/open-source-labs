# Personalizar o gráfico

Nesta etapa, personalizaremos o gráfico de hastes 3D alterando a linha de base (baseline) usando o parâmetro `bottom` e alterando o formato usando os parâmetros `linefmt`, `markerfmt` e `basefmt`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
