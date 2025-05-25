# Carregar Dados

Vamos carregar dados do conjunto de dados `20newsgroups`, que compreende cerca de 18.000 mensagens de grupos de notícias sobre 20 tópicos divididos em dois subconjuntos: um para treino e outro para teste. Por simplicidade e para reduzir o custo computacional, selecionamos um subconjunto de 7 tópicos e usamos apenas o conjunto de treino.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "misc.forsale",
    "rec.autos",
    "sci.space",
    "talk.religion.misc",
]

print("Carregando dados de treino do 20 newsgroups")
raw_data, _ = fetch_20newsgroups(subset="train", categories=categories, return_X_y=True)
data_size_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6
print(f"{len(raw_data)} documentos - {data_size_mb:.3f}MB")
```
