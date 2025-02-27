# Benchmarking von Klassifizierern

Wir werden nun die Datensätze mit acht verschiedenen Klassifikationsmodellen trainieren und testen und die Leistungsergebnisse für jedes Modell erhalten. Ziel dieser Studie ist es, die Rechenleistung/Genauigkeit-Abstimmung verschiedener Typen von Klassifizierern für ein solches mehrklassenes Textklassifizierungsproblem zu verdeutlichen.

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
    (LogisticRegression(C=5, max_iter=1000), "Logistische Regression"),
    (RidgeClassifier(alpha=1.0, solver="sparse_cg"), "Ridge-Klassifizierer"),
    (KNeighborsClassifier(n_neighbors=100), "kNN"),
    (RandomForestClassifier(), "Random Forest"),
    # L2 Strafmaß Linear SVC
    (LinearSVC(C=0.1, dual=False, max_iter=1000), "Linear SVC"),
    # L2 Strafmaß Linear SGD
    (
        SGDClassifier(
            loss="log_loss", alpha=1e-4, n_iter_no_change=3, early_stopping=True
        ),
        "log-loss SGD",
    ),
    # NearestCentroid (aka Rocchio-Klassifizierer)
    (NearestCentroid(), "NearestCentroid"),
    # Sparse naive Bayes-Klassifizierer
    (ComplementNB(alpha=0.1), "Complement naive Bayes"),
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
    title="Score-Trainingszeit-Abstimmung",
    yscale="log",
    xlabel="Testgenauigkeit",
    ylabel="Trainingszeit (s)",
)
fig, ax2 = plt.subplots(figsize=(10, 8))
ax2.scatter(score, test_time, s=60)
ax2.set(
    title="Score-Testzeit-Abstimmung",
    yscale="log",
    xlabel="Testgenauigkeit",
    ylabel="Testzeit (s)",
)

for i, txt in enumerate(clf_names):
    ax1.annotate(txt, (score[i], training_time[i]))
    ax2.annotate(txt, (score[i], test_time[i]))
```
