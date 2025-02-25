# Eliminar componentes individuales

Podemos eliminar componentes individuales del diagrama de caja utilizando los diversos argumentos de palabras clave disponibles en la función `boxplot()`. Por ejemplo, podemos eliminar las medias estableciendo `showmeans` en False. También podemos eliminar la caja y las bigotes estableciendo `showbox` y `showcaps` en False, respectivamente.

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
