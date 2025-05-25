# Criar Grupo de Espécies

Neste passo, criaremos um grupo com informações sobre um organismo específico. Criaremos uma função chamada `create_species_bunch` que recebe o nome da espécie, dados de treino (`train`), dados de teste (`test`), dados de cobertura (`coverages`), e as grades `xgrid` e `ygrid` como entrada e retorna um objeto `bunch`.

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """Criar um grupo com informações sobre um organismo específico

    Isto utilizará os arrays de registros de teste/treino para extrair os
    dados específicos para o nome da espécie fornecido.
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # escolher pontos associados à espécie desejada
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # determinar os valores de cobertura para cada um dos pontos de treino e teste
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# Criar grupos de espécies
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```
