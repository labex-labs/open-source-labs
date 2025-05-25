# Avaliação

Avaliaremos os classificadores com várias métricas de classificação: brier_score_loss, log_loss, precisão, revocação, pontuação F1 e AUC ROC.

```python
from collections import defaultdict

import pandas as pd

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    brier_score_loss,
    log_loss,
    roc_auc_score,
)

scores = defaultdict(list)
for i, (clf, name) in enumerate(clf_list):
    clf.fit(X_train, y_train)
    y_prob = clf.predict_proba(X_test)
    y_pred = clf.predict(X_test)
    scores["Classificador"].append(name)

    for metric in [brier_score_loss, log_loss, roc_auc_score]:
        nome_métrica = metric.__name__.replace("_", " ").replace("score", "").capitalize()
        scores[nome_métrica].append(metric(y_test, y_prob[:, 1]))

    for metric in [precision_score, recall_score, f1_score]:
        nome_métrica = metric.__name__.replace("_", " ").replace("score", "").capitalize()
        scores[nome_métrica].append(metric(y_test, y_pred))

    score_df = pd.DataFrame(scores).set_index("Classificador")
    score_df.round(decimals=3)
```
