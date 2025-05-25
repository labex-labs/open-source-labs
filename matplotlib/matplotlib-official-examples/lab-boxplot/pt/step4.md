# Remover Componentes Individuais

Podemos remover componentes individuais do box plot usando os vários argumentos de palavra-chave disponíveis na função `boxplot()`. Por exemplo, podemos remover as médias definindo `showmeans` como False. Também podemos remover a caixa e os "whiskers" (arestas) definindo `showbox` e `showcaps` como False, respectivamente.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

axs[0, 1].boxplot(data, labels=labels, showmeans=False)
axs[0, 1].set_title('No Means')

axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axs[1, 0].set_title('No Box or Whiskers')

axs[1, 1].boxplot(data, labels=labels, showfliers=False)
axs[1, 1].set_title('No Outliers')

plt.show()
```
