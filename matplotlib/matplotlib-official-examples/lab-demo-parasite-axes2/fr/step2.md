# Création d'axes hôtes et parasites

Nous allons créer un axe hôte et deux axes parasites à l'aide des fonctions `host_subplot()` et `twinx()`. La fonction `host_subplot()` crée un axe hôte, et la fonction `twinx()` crée des axes parasites qui partagent le même axe x que l'axe hôte.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
