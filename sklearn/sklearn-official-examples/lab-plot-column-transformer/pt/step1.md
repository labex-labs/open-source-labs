# Conjunto de Dados

Utilizaremos o conjunto de dados 20 newsgroups, que consiste em mensagens de grupos de notícias sobre 20 tópicos. O conjunto de dados é dividido em subconjuntos de treino e teste com base nas mensagens publicadas antes e depois de uma data específica. Utilizaremos apenas mensagens de 2 categorias para acelerar o tempo de execução.

```python
categories = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```
