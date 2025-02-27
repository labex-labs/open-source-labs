# Créer un Bunch d'espèces

Dans cette étape, nous allons créer un bunch avec des informations sur un organisme particulier. Nous allons créer une fonction appelée create_species_bunch qui prend le nom de l'espèce, les ensembles d'entraînement et de test, les couvertures, xgrid et ygrid en entrée et renvoie un objet bunch.

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """Créer un bunch avec des informations sur un organisme particulier

    Cela utilisera les tableaux d'enregistrements d'entraînement/test pour extraire
    les données spécifiques au nom d'espèce donné.
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # choisir les points associés à l'espèce souhaitée
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # déterminer les valeurs de couverture pour chacun des points d'entraînement et de test
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# Créer un bunch d'espèces
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```
