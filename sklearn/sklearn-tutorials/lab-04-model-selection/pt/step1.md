# Pontuação e Pontuações Validadas Cruzadamente

Os estimadores no scikit-learn expõem um método `score` que pode ser usado para avaliar a qualidade do ajuste do modelo ou a previsão em novos dados. Este método retorna uma pontuação, onde um valor mais alto indica um melhor desempenho.

```python
from sklearn import datasets, svm

# Carregar o conjunto de dados dígitos
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# Criar um classificador SVM com núcleo linear
svc = svm.SVC(C=1, kernel='linear')

# Ajustar o classificador nos dados de treino e calcular a pontuação nos dados de teste
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

Para obter uma melhor medida da precisão da previsão, podemos usar a validação cruzada. A validação cruzada envolve dividir os dados em múltiplos folds, usando cada fold como conjunto de teste e os folds restantes como conjuntos de treino. Este processo é repetido várias vezes, e as pontuações são médias para obter o desempenho geral.

```python
import numpy as np

# Dividir os dados em 3 folds
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# Executar validação cruzada
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
