# Formateur par défaut

Nous commençons par examiner le formateur par défaut et sa sortie verbeuse. Nous traçons des données en fonction du temps et observons comment le formateur par défaut affiche la date et l'heure.

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# créer des données temporelles
base = datetime.datetime(2005, 2, 1)
dates = [base + datetime.timedelta(hours=(2 * i)) for i in range(732)]
N = len(dates)
np.random.seed(19680801)
y = np.cumsum(np.random.randn(N))

# tracer les données
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
lims = [(np.datetime64('2005-02'), np.datetime64('2005-04')),
        (np.datetime64('2005-02-03'), np.datetime64('2005-02-15')),
        (np.datetime64('2005-02-03 11:00'), np.datetime64('2005-02-04 13:20'))]
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
    # rotation des étiquettes...
    for label in ax.get_xticklabels():
        label.set_rotation(40)
        label.set_horizontalalignment('right')
axs[0].set_title('Formateur de date par défaut')
plt.show()
```
