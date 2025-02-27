# Codificación de etiquetas

La codificación de etiquetas es el proceso de convertir etiquetas no numéricas en etiquetas numéricas. Esto se puede lograr utilizando la clase `LabelEncoder`.

```python
from sklearn import preprocessing

# Crea una instancia de LabelEncoder
le = preprocessing.LabelEncoder()

# Ajusta el LabelEncoder a una lista de etiquetas no numéricas
le.fit(["parís", "parís", "tokio", "ámsterdam"])

# Obtiene las clases aprendidas por el LabelEncoder
list(le.classes_)

# Transforma una lista de etiquetas no numéricas en etiquetas numéricas
le.transform(["tokio", "tokio", "parís"])

# Invierte la transformación de etiquetas numéricas de vuelta a etiquetas no numéricas
list(le.inverse_transform([2, 2, 1]))
```
