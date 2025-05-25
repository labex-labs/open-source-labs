# Carregando os Dados de Texto

Primeiro, precisamos carregar os dados de texto com os quais trabalharemos. Usaremos o conjunto de dados 20 Newsgroups, que contém artigos de notícias de vinte tópicos diferentes. Para carregar o conjunto de dados, podemos usar a função `fetch_20newsgroups` do scikit-learn.

```python
from sklearn.datasets import fetch_20newsgroups

# Carregar o conjunto de dados
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

Agora que carregamos os dados, podemos explorar sua estrutura e conteúdo.
