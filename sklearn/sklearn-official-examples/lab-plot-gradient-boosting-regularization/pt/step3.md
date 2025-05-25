# Definir Parâmetros

Vamos definir os parâmetros para o nosso Classificador de Reforço Gradiente. Usaremos os seguintes parâmetros:

- `n_estimators`: número de etapas de reforço a serem executadas
- `max_leaf_nodes`: número máximo de nós folha em cada árvore
- `max_depth`: profundidade máxima da árvore
- `random_state`: semente aleatória para consistência
- `min_samples_split`: número mínimo de amostras necessárias para dividir um nó interno

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```
