# Trazar la curva Precision-Recall para la clasificación multi-etiqueta

La curva Precision-Recall no admite el caso de clasificación multi-etiqueta. Sin embargo, se puede decidir cómo manejar este caso. Crearemos un conjunto de datos multi-etiqueta, ajustaremos y predeciremos utilizando OneVsRestClassifier y luego trazaremos la curva Precision-Recall.

```python
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score

# Crear datos multi-etiqueta
Y = label_binarize(y, classes=[0, 1, 2])
n_classes = Y.shape[1]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=random_state
)

# Ajustar y predecir utilizando OneVsRestClassifier
classifier = OneVsRestClassifier(
    make_pipeline(StandardScaler(), LinearSVC(random_state=random_state, dual="auto"))
)
classifier.fit(X_train, Y_train)
y_score = classifier.decision_function(X_test)

# Calcular precisión y recuperación para cada clase
precision = dict()
recall = dict()
average_precision = dict()
for i in range(n_classes):
    precision[i], recall[i], _ = precision_recall_curve(Y_test[:, i], y_score[:, i])
    average_precision[i] = average_precision_score(Y_test[:, i], y_score[:, i])

# Calcular precisión y recuperación micro-promediadas
precision["micro"], recall["micro"], _ = precision_recall_curve(Y_test.ravel(), y_score.ravel())
average_precision["micro"] = average_precision_score(Y_test, y_score, average="micro")

# Trazar la curva Precision-Recall micro-promediada
display = PrecisionRecallDisplay(
    recall=recall["micro"],
    precision=precision["micro"],
    average_precision=average_precision["micro"],
    prevalence_pos_label=Counter(Y_test.ravel())[1] / Y_test.size,
)
display.plot(plot_chance_level=True)
_ = display.ax_.set_title("Micro-promediado sobre todas las clases")

# Trazar la curva Precision-Recall para cada clase y curvas iso-f1
colors = cycle(["navy", "turquoise", "darkorange", "cornflowerblue", "teal"])
_, ax = plt.subplots(figsize=(7, 8))
f_scores = np.linspace(0.2, 0.8, num=4)
lines, labels = [], []
for f_score in f_scores:
    x = np.linspace(0.01, 1)
    y = f_score * x / (2 * x - f_score)
    (l,) = plt.plot(x[y >= 0], y[y >= 0], color="gray", alpha=0.2)
    plt.annotate("f1={0:0.1f}".format(f_score), xy=(0.9, y[45] + 0.02))

display = PrecisionRecallDisplay(
    recall=recall["micro"],
    precision=precision["micro"],
    average_precision=average_precision["micro"],
)
display.plot(ax=ax, name="Precisión-recuperación micro-promedio", color="gold")

for i, color in zip(range(n_classes), colors):
    display = PrecisionRecallDisplay(
        recall=recall[i],
        precision=precision[i],
        average_precision=average_precision[i],
    )
    display.plot(ax=ax, name=f"Precisión-recuperación para la clase {i}", color=color)

handles, labels = display.ax_.get_legend_handles_labels()
handles.extend([l])
labels.extend(["curvas iso-f1"])
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.legend(handles=handles, labels=labels, loc="best")
ax.set_title("Extensión de la curva Precision-Recall a multi-clase")
plt.show()
```
