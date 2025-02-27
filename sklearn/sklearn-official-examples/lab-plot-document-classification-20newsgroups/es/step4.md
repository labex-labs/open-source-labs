# Evaluación de clasificadores

Ahora entrenaremos y probaremos los conjuntos de datos con ocho diferentes modelos de clasificación y obtendremos los resultados de rendimiento para cada modelo. El objetivo de este estudio es resaltar los trade-offs entre cálculo y precisión de diferentes tipos de clasificadores para un problema de clasificación de texto multi-clase.

```python
from sklearn.utils.extmath import density
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import ComplementNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier

results = []
for clf, name in (
    (LogisticRegression(C=5, max_iter=1000), "Regresión Logística"),
    (RidgeClassifier(alpha=1.0, solver="sparse_cg"), "Clasificador Ridge"),
    (KNeighborsClassifier(n_neighbors=100), "kNN"),
    (RandomForestClassifier(), "Bosque Aleatorio"),
    # L2 penalty Linear SVC
    (LinearSVC(C=0.1, dual=False, max_iter=1000), "SVC Lineal"),
    # L2 penalty Linear SGD
    (
        SGDClassifier(
            loss="log_loss", alpha=1e-4, n_iter_no_change=3, early_stopping=True
        ),
        "SGD con log-loss",
    ),
    # NearestCentroid (aka Rocchio classifier)
    (NearestCentroid(), "Centroide más cercano"),
    # Sparse naive Bayes classifier
    (ComplementNB(alpha=0.1), "Naive Bayes Complementario"),
):
    print("=" * 80)
    print(name)
    results.append(benchmark(clf, name))

indices = np.arange(len(results))

results = [[x[i] for x in results] for i in range(4)]

clf_names, score, training_time, test_time = results
training_time = np.array(training_time)
test_time = np.array(test_time)

fig, ax1 = plt.subplots(figsize=(10, 8))
ax1.scatter(score, training_time, s=60)
ax1.set(
    title="Trade-off entre puntuación y tiempo de entrenamiento",
    yscale="log",
    xlabel="precisión de prueba",
    ylabel="tiempo de entrenamiento (s)",
)
fig, ax2 = plt.subplots(figsize=(10, 8))
ax2.scatter(score, test_time, s=60)
ax2.set(
    title="Trade-off entre puntuación y tiempo de prueba",
    yscale="log",
    xlabel="precisión de prueba",
    ylabel="tiempo de prueba (s)",
)

for i, txt in enumerate(clf_names):
    ax1.annotate(txt, (score[i], training_time[i]))
    ax2.annotate(txt, (score[i], test_time[i]))
```
