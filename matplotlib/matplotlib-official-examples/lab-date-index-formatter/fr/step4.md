# Utilisation d'un objet appelable pour le formateur

Au lieu de passer une fonction à `.Axis.set_major_formatter`, nous pouvons utiliser tout autre objet appelable, tel qu'une instance d'une classe qui implémente `__call__`. Dans cette étape, nous allons créer une classe `MyFormatter` qui formatera les repères d'échelle en tant que dates.

```python
# Utiliser un objet appelable pour le formateur
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Retourne l'étiquette pour l'heure x à la position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
