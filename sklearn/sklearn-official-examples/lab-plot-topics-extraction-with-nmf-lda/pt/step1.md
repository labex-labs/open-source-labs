# Carregar o Conjunto de Dados

Vamos carregar o conjunto de dados 20 newsgroups e vetorizá-lo. Usamos algumas heurísticas para filtrar termos inúteis desde o início: os posts são desprovidos de cabeçalhos, rodapés e respostas citadas, e palavras comuns em inglês, palavras que aparecem em apenas um documento ou em pelo menos 95% dos documentos são removidas.

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Carregando conjunto de dados...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
