# Comparação de Classificadores

Agora, treinaremos e testaremos os conjuntos de dados com oito modelos de classificação diferentes e obteremos os resultados de desempenho para cada modelo. O objetivo deste estudo é destacar os trade-offs entre computação e precisão de diferentes tipos de classificadores para um problema de classificação de texto multiclasse.

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
    (LogisticRegression(C=5, max_iter=1000), "Regressão Logística"),
    (RidgeClassifier(alpha=1.0, solver="sparse_cg"), "Classificador Ridge"),
    (KNeighborsClassifier(n_neighbors=100), "kNN"),
    (RandomForestClassifier(), "Floresta Aleatória"),
    # Linear SVC com penalidade L2
    (LinearSVC(C=0.1, dual=False, max_iter=1000), "Linear SVC"),
    # Linear SGD com penalidade L2
    (
        SGDClassifier(
            loss="log_loss", alpha=1e-4, n_iter_no_change=3, early_stopping=True
        ),
        "SGD com log-loss",
    ),
    # NearestCentroid (também conhecido como classificador Rocchio)
    (NearestCentroid(), "NearestCentroid"),
    # Classificador Naive Bayes esparso
    (ComplementNB(alpha=0.1), "Naive Bayes Complementar"),
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
    title="Trade-off entre Precisão e Tempo de Treinamento",
    yscale="log",
    xlabel="Precisão no teste",
    ylabel="Tempo de treinamento (s)",
)
fig, ax2 = plt.subplots(figsize=(10, 8))
ax2.scatter(score, test_time, s=60)
ax2.set(
    title="Trade-off entre Precisão e Tempo de Teste",
    yscale="log",
    xlabel="Precisão no teste",
    ylabel="Tempo de teste (s)",
)

for i, txt in enumerate(clf_names):
    ax1.annotate(txt, (score[i], training_time[i]))
    ax2.annotate(txt, (score[i], test_time[i]))
```
