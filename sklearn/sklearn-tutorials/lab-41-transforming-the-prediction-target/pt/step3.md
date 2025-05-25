# Codificação de Rótulos

A codificação de rótulos é o processo de converter rótulos não numéricos em rótulos numéricos. Isso pode ser feito usando a classe `LabelEncoder`.

```python
from sklearn import preprocessing

# Crie uma instância de LabelEncoder
le = preprocessing.LabelEncoder()

# Ajuste o LabelEncoder em uma lista de rótulos não numéricos
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# Obtenha as classes aprendidas pelo LabelEncoder
list(le.classes_)

# Transforme uma lista de rótulos não numéricos em rótulos numéricos
le.transform(["tokyo", "tokyo", "paris"])

# Transforme inversamente os rótulos numéricos de volta para rótulos não numéricos
list(le.inverse_transform([2, 2, 1]))
```
