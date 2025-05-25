# Selecionando Características com Seleção Sequencial de Características

Utilizamos o Selecionador Sequencial de Características (SFS) para selecionar as características. O SFS é um procedimento guloso onde, em cada iteração, escolhemos a melhor nova característica a adicionar às nossas características selecionadas com base numa pontuação de validação cruzada. Também podemos ir na direção inversa (SFS reversa), ou seja, começar com todas as características e escolher gulosamente as características a remover uma a uma.

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Características selecionadas pela seleção sequencial direta: {feature_names[sfs_forward.get_support()]}")
print(f"Características selecionadas pela seleção sequencial reversa: {feature_names[sfs_backward.get_support()]}")
```
