# Criando um Gráfico de Caixa Entalhado (Notched Box Plot)

Agora criaremos um gráfico de caixa entalhado com a função `boxplot()`. Definiremos o parâmetro `notch` como `True` para criar um gráfico de caixa entalhado.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax2.set_title('Notched Box Plot')
```
