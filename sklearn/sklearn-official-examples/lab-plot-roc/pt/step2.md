# ROC Multiclasses Um-Contra-Todos

A estratégia multiclasses Um-Contra-Todos (OvR) consiste em calcular uma curva ROC para cada uma das `n_classes`. Em cada passo, uma classe específica é considerada como a classe positiva e as restantes classes são consideradas como a classe negativa em conjunto. Neste passo, mostramos como calcular a curva ROC utilizando a estratégia multiclasses OvR.

```python
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

# Binarizar o alvo usando a estratégia OvR
label_binarizer = LabelBinarizer().fit(y_train)
y_onehot_test = label_binarizer.transform(y_test)

# Treinar um modelo de Regressão Logística
classifier = LogisticRegression()
y_score = classifier.fit(X_train, y_train).predict_proba(X_test)

# Calcular a curva ROC e a pontuação ROC AUC para cada classe
fpr, tpr, roc_auc = dict(), dict(), dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_onehot_test[:, i], y_score[:, i])
    roc_auc[i] = roc_auc_score(y_onehot_test[:, i], y_score[:, i])

# Calcular a curva ROC e a área ROC da média micro
fpr["micro"], tpr["micro"], _ = roc_curve(y_onehot_test.ravel(), y_score.ravel())
roc_auc["micro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="micro")

# Calcular a curva ROC e a área ROC da média macro
# Agregar as taxas de verdadeiros/falsos positivos por classe
fpr["macro"], tpr["macro"] = [], []
for i in range(n_classes):
    fpr_averaged, tpr_averaged = [], []
    for j in range(n_classes):
        if i != j:
            fpr_averaged += list(fpr[j])
            tpr_averaged += list(tpr[j])
    fpr_averaged = np.array(fpr_averaged)
    tpr_averaged = np.array(tpr_averaged)
    fpr["macro"].append(fpr_averaged)
    tpr["macro"].append(tpr_averaged)
fpr["macro"] = np.concatenate(fpr["macro"])
tpr["macro"] = np.concatenate(tpr["macro"])
roc_auc["macro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="macro")

# Plotar as curvas ROC para cada classe e as médias micro/macro
fig, ax = plt.subplots(figsize=(6, 6))
colors = ["aqua", "darkorange", "cornflowerblue"]
for i, color in zip(range(n_classes), colors):
    RocCurveDisplay.from_predictions(
        y_onehot_test[:, i],
        y_score[:, i],
        name=f"Curva ROC da classe {target_names[i]} (AUC = {roc_auc[i]:.2f})",
        color=color,
        ax=ax,
        plot_micro=False,
        plot_macro=False,
    )

RocCurveDisplay.from_predictions(
    y_onehot_test.ravel(),
    y_score.ravel(),
    name=f"Curva ROC da média micro (AUC = {roc_auc['micro']:.2f})",
    color="deeppink",
    linestyle=":",
    linewidth=4,
    ax=ax,
)

plt.plot(
    fpr["macro"],
    tpr["macro"],
    label=f"Curva ROC da média macro (AUC = {roc_auc['macro']:.2f})",
    color="navy",
    linestyle=":",
    linewidth=4,
)

plt.plot([0, 1], [0, 1], "k--", label="Nível de acaso")
plt.axis("square")
plt.xlabel("Taxa de Falsos Positivos")
plt.ylabel("Taxa de Verdadeiros Positivos")
plt.title("Curvas ROC Um-Contra-Todos")
plt.legend()
plt.show()
```
