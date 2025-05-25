# Plotar Curvas de Calibração

Treinamos cada um dos quatro modelos com o pequeno conjunto de dados de treino e plotamos as curvas de calibração usando as probabilidades previstas do conjunto de dados de teste. As curvas de calibração são criadas agrupando as probabilidades previstas, em seguida, plotando a probabilidade média prevista em cada grupo contra a frequência observada ('fracção de positivos'). Abaixo da curva de calibração, plotamos um histograma que mostra a distribuição das probabilidades previstas ou, mais especificamente, o número de amostras em cada grupo de probabilidade prevista.

```python
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibrationDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Criar classificadores
lr = LogisticRegression()
gnb = GaussianNB()
svc = NaivelyCalibratedLinearSVC(C=1.0, dual="auto")
rfc = RandomForestClassifier()

clf_list = [
    (lr, "Regressão Logística"),
    (gnb, "Naive Bayes"),
    (svc, "SVC"),
    (rfc, "Floresta Aleatória"),
]

fig = plt.figure(figsize=(10, 10))
gs = GridSpec(4, 2)
colors = plt.get_cmap("Dark2")

ax_calibration_curve = fig.add_subplot(gs[:2, :2])
calibration_displays = {}
markers = ["^", "v", "s", "o"]
for i, (clf, name) in enumerate(clf_list):
    clf.fit(X_train, y_train)
    display = CalibrationDisplay.from_estimator(
        clf,
        X_test,
        y_test,
        n_bins=10,
        name=name,
        ax=ax_calibration_curve,
        color=colors(i),
        marker=markers[i],
    )
    calibration_displays[name] = display

ax_calibration_curve.grid()
ax_calibration_curve.set_title("Gráficos de Calibração")

# Adicionar histograma
grid_positions = [(2, 0), (2, 1), (3, 0), (3, 1)]
for i, (_, name) in enumerate(clf_list):
    row, col = grid_positions[i]
    ax = fig.add_subplot(gs[row, col])

    ax.hist(
        calibration_displays[name].y_prob,
        range=(0, 1),
        bins=10,
        label=name,
        color=colors(i),
    )
    ax.set(title=name, xlabel="Probabilidade média prevista", ylabel="Contagem")

plt.tight_layout()
plt.show()
```
