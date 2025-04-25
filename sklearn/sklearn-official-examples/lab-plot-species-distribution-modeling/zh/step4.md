# 创建物种集合物

在这一步中，我们将创建一个包含特定生物体信息的集合物。我们将创建一个名为 create_species_bunch 的函数，该函数以物种名称、训练集、测试集、覆盖范围、x 网格和 y 网格作为输入，并返回一个集合物对象。

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """创建一个包含特定生物体信息的集合物

    这将使用测试/训练记录数组来提取
    与给定物种名称相关的数据。
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # 选择与所需物种相关的点
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # 确定每个训练和测试点的覆盖值
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# 创建物种集合物
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```
