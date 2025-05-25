# Criando um Gráfico de Caixa Retangular (Rectangular Box Plot)

Agora criaremos um gráfico de caixa retangular usando a função `boxplot()` em Matplotlib. Definiremos o parâmetro `patch_artist` como `True` para preencher a caixa com cor.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax1.set_title('Rectangular Box Plot')
```
