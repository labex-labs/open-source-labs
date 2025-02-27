# Crear el grupo de especies

En este paso, crearemos un grupo con información sobre un organismo particular. Crearemos una función llamada create_species_bunch que toma el nombre de la especie, train, test, coverages, xgrid e ygrid como entrada y devuelve un objeto grupo.

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """Crear un grupo con información sobre un organismo particular

    Esto usará las matrices de registros de prueba/train para extraer
    los datos específicos del nombre de la especie dado.
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # elegir puntos asociados con la especie deseada
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # determinar los valores de cobertura para cada uno de los puntos de entrenamiento y prueba
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# Crear el grupo de especies
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```
