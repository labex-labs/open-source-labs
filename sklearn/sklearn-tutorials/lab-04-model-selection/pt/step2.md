# Geradores de Validação Cruzada

O scikit-learn fornece uma coleção de classes que podem ser usadas para gerar índices de treino/teste para estratégias populares de validação cruzada. Estas classes têm um método `split` que aceita o conjunto de dados de entrada e gera os índices de conjunto de treino/teste para cada iteração do processo de validação cruzada.

```python
from sklearn.model_selection import KFold

# Dividir os dados em K folds usando a validação cruzada KFold
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Treino: {train_indices} | teste: {test_indices}')
```

A função auxiliar `cross_val_score` pode ser usada para calcular a pontuação de validação cruzada diretamente. Ela divide os dados em conjuntos de treino e teste para cada iteração da validação cruzada, treina o estimador no conjunto de treino e calcula a pontuação com base no conjunto de teste.

```python
from sklearn.model_selection import cross_val_score

# Calcular a pontuação de validação cruzada para o classificador SVM
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
