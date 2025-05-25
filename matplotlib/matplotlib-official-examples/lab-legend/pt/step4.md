# Adicionando a Legenda

Para adicionar a legenda ao nosso gráfico, usamos a função `legend` do Matplotlib. Passamos o parâmetro `loc` para especificar a localização da legenda e o parâmetro `shadow` para adicionar um efeito de sombra à legenda. Também usamos o parâmetro `fontsize` para definir o tamanho da fonte da legenda.

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```
