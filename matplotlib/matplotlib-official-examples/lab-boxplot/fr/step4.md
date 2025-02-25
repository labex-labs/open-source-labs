# Supprimer les composants individuels

Nous pouvons supprimer les composants individuels du diagramme en boîte en utilisant les différents arguments clés disponibles dans la fonction `boxplot()`. Par exemple, nous pouvons supprimer les moyennes en définissant `showmeans` sur False. Nous pouvons également supprimer la boîte et les barres d'erreur en définissant respectivement `showbox` et `showcaps` sur False.

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
