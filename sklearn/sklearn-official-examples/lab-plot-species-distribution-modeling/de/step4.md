# Arten-Bunch erstellen

In diesem Schritt werden wir ein Bunch mit Informationen über ein bestimmtes Organismus erstellen. Wir werden eine Funktion namens create_species_bunch erstellen, die den Artenamen, train, test, coverages, xgrid und ygrid als Eingabe nimmt und ein Bunch-Objekt zurückgibt.

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """Erstelle ein Bunch mit Informationen über ein bestimmtes Organismus

    Dies wird die Test-/Trainings-Aufzeichnungsmengen verwenden, um die
    Daten für den angegebenen Artenamen zu extrahieren.
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # wähle die Punkte, die mit der gewünschten Art assoziiert sind
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # bestimme die Coverage-Werte für jeden der Trainings- und Testpunkte
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# Erstelle Arten-Bunch
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```
