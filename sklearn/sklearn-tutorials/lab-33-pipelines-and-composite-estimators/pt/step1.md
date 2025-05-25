# Pipeline - Encadeamento de Estimadores

A classe `Pipeline` no scikit-learn é usada para encadear múltiplos estimadores num único objeto. Isto permite chamar `fit` e `predict` uma única vez nos seus dados para ajustar uma sequência completa de estimadores. Também permite a seleção conjunta de parâmetros e ajuda a evitar vazamentos de dados na validação cruzada.

Para criar um pipeline, é necessário fornecer uma lista de pares `(chave, valor)`, onde a `chave` é uma string para identificar cada passo e o `valor` é um objeto estimador. Abaixo está um exemplo de criação de um pipeline com um transformador PCA e um classificador SVM:

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

Pode aceder aos passos de um pipeline usando indexação ou por nome:

```python
pipe.steps[0]  # acesso por índice
pipe[0]  # equivalente ao anterior
pipe['reduce_dim']  # acesso por nome
```

Também pode usar a função `make_pipeline` como uma forma abreviada de construir pipelines:

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```
