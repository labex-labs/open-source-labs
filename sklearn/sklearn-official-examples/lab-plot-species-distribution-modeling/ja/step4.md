# 種のバンチを作成する

このステップでは、特定の生物に関する情報を持つバンチを作成します。種名、学習用データ、テスト用データ、カバレッジ、x グリッド、y グリッドを入力として受け取り、バンチオブジェクトを返す create_species_bunch という関数を作成します。

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """Create a bunch with information about a particular organism

    This will use the test/train record arrays to extract the
    data specific to the given species name.
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # choose points associated with the desired species
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # determine coverage values for each of the training & testing points
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# Create species bunch
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```
