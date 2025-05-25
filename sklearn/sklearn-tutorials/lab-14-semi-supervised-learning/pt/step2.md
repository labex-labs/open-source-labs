# Auto-Treino

#### Visão Geral do algoritmo de Auto-Treino

O algoritmo de Auto-Treino baseia-se no algoritmo de Yarowsky. Permite que um classificador supervisionado funcione como um classificador semi-supervisionado, aprendendo com dados não rotulados. O algoritmo funciona iterativamente treinando o classificador supervisionado nos dados rotulados e não rotulados e, em seguida, usando as previsões nos dados não rotulados para adicionar um subconjunto dessas amostras aos dados rotulados. O algoritmo continua iterando até que todas as amostras tenham rótulos ou nenhuma nova amostra seja selecionada numa iteração.

#### Utilizando o Auto-Treino no scikit-learn

No scikit-learn, o algoritmo de Auto-Treino é implementado na classe `SelfTrainingClassifier`. Para utilizar este algoritmo, é necessário fornecer um classificador supervisionado que implemente o método `predict_proba`. Aqui está um exemplo de como utilizar o algoritmo de Auto-Treino:

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# Crie um classificador de regressão logística
classificador = LogisticRegression()

# Crie um classificador de auto-treino com o classificador de regressão logística como classificador base
classificador_auto_treino = SelfTrainingClassifier(classificador)

# Treine o classificador de auto-treino nos dados rotulados e não rotulados
classificador_auto_treino.fit(X_labeled, y_labeled, X_unlabeled)

# Preveja os rótulos para novas amostras
y_pred = classificador_auto_treino.predict(X_test)
```

No exemplo acima, `X_labeled` e `y_labeled` são os dados rotulados, `X_unlabeled` são os dados não rotulados e `X_test` são as novas amostras a serem previstas.
