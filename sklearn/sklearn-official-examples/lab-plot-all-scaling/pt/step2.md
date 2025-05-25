# Selecionar Recursos e Definir Mapeamento de Recursos

Em seguida, selecionamos dois recursos do conjunto de dados para facilitar a visualização e definimos um mapeamento dos nomes dos recursos para uma melhor visualização.

```python
# Selecionar dois recursos
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# Definir mapeamento de recursos
feature_mapping = {
    "MedInc": "Rendimento médio no bloco",
    "AveOccup": "Ocupação média de casas",
}
```
