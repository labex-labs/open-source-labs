# Binário de Rótulos

A binarização de rótulos é o processo de conversão de rótulos multiclasse em uma matriz indicadora binária. Isso pode ser alcançado usando a classe `LabelBinarizer`.

```python
from sklearn import preprocessing

# Crie uma instância de LabelBinarizer
lb = preprocessing.LabelBinarizer()

# Ajuste o LabelBinarizer em uma lista de rótulos multiclasse
lb.fit([1, 2, 6, 4, 2])

# Obtenha as classes aprendidas pelo LabelBinarizer
lb.classes_

# Transforme uma lista de rótulos multiclasse em uma matriz indicadora binária
lb.transform([1, 6])
```
