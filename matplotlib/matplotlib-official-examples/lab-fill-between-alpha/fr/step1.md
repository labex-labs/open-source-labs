# Amélioration d'un graphique en ligne avec `fill_between`

Le premier exemple montre comment améliorer un graphique en ligne avec `fill_between`. Nous utiliserons des données financières de Google pour créer deux sous-graphiques, l'un avec un simple graphique en ligne et l'autre avec un graphique en ligne rempli.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# chargez quelques données financières d'échantillonnage
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)

# créez deux sous-graphiques avec les axes x et y partagés
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

pricemin = r.close.min()

ax1.plot(r.date, r.close, lw=2)
ax2.fill_between(r.date, pricemin, r.close, alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('prix')
fig.suptitle('Prix de clôture quotidien de Google (GOOG)')
fig.autofmt_xdate()
```
