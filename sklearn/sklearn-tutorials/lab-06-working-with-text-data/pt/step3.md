# Extração de Recursos

Para representar os dados de texto como vetores de recursos, podemos usar a representação de "sacos de palavras". Essa representação atribui um ID inteiro fixo a cada palavra no conjunto de treinamento e conta o número de ocorrências de cada palavra em cada documento. Podemos extrair esses vetores de recursos usando o `CountVectorizer` do scikit-learn.

```python
from sklearn.feature_extraction.text import CountVectorizer

# Extrair vetores de recursos
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

Agora que extraímos os vetores de recursos, podemos usá-los para treinar nosso modelo.
