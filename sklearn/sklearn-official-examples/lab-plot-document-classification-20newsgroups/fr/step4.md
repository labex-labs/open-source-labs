# Évaluation comparative de classifieurs

Nous allons maintenant entraîner et tester les ensembles de données avec huit modèles de classification différents et obtenir les résultats de performance de chaque modèle. L'objectif de cette étude est de mettre en évidence les compromis entre calcul et précision pour différents types de classifieurs dans le cadre d'un problème de classification de texte multi-classe.

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
    (LogisticRegression(C=5, max_iter=1000), "Régression logistique"),
    (RidgeClassifier(alpha=1.0, solver="sparse_cg"), "Classifieur Ridge"),
    (KNeighborsClassifier(n_neighbors=100), "kNN"),
    (RandomForestClassifier(), "Forêt aléatoire"),
    # L2 penalty Linear SVC
    (LinearSVC(C=0.1, dual=False, max_iter=1000), "SVC linéaire"),
    # L2 penalty Linear SGD
    (
        SGDClassifier(
            loss="log_loss", alpha=1e-4, n_iter_no_change=3, early_stopping=True
        ),
        "SGD avec log-loss",
    ),
    # NearestCentroid (aka Rocchio classifier)
    (NearestCentroid(), "Centroïde le plus proche"),
    # Sparse naive Bayes classifier
    (ComplementNB(alpha=0.1), "Naive Bayes complémentaire"),
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
    title="Compromis entre score et temps d'entraînement",
    yscale="log",
    xlabel="précision sur le test",
    ylabel="temps d'entraînement (s)",
)
fig, ax2 = plt.subplots(figsize=(10, 8))
ax2.scatter(score, test_time, s=60)
ax2.set(
    title="Compromis entre score et temps de test",
    yscale="log",
    xlabel="précision sur le test",
    ylabel="temps de test (s)",
)

for i, txt in enumerate(clf_names):
    ax1.annotate(txt, (score[i], training_time[i]))
    ax2.annotate(txt, (score[i], test_time[i]))
```
