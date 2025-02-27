# Datenaufbereitung

Der erste Schritt besteht darin, die Datensatz aufzubereiten. In diesem Beispiel verwenden wir reale Datensätze aus dem `datasets`-Modul von Scikit-Learn. Die Stichprobengröße einiger Datensätze wird reduziert, um die Berechnung zu beschleunigen. Nach der Datenaufbereitung werden die Ziele der Datensätze zwei Klassen haben, wobei 0 für Inlier und 1 für Ausreißer steht. Die `preprocess_dataset`-Funktion gibt Daten und Ziel zurück.

```python
import numpy as np
from sklearn.datasets import fetch_kddcup99, fetch_covtype, fetch_openml
from sklearn.preprocessing import LabelBinarizer
import pandas as pd

rng = np.random.RandomState(42)

def preprocess_dataset(dataset_name):
    # Laden und Vektorisierung
    print(f"Lade {dataset_name} Daten")
    if dataset_name in ["http", "smtp", "SA", "SF"]:
        dataset = fetch_kddcup99(subset=dataset_name, percent10=True, random_state=rng)
        X = dataset.data
        y = dataset.target
        lb = LabelBinarizer()

        if dataset_name == "SF":
            idx = rng.choice(X.shape[0], int(X.shape[0] * 0.1), replace=False)
            X = X[idx]  # Stichprobengröße reduzieren
            y = y[idx]
            x1 = lb.fit_transform(X[:, 1].astype(str))
            X = np.c_[X[:, :1], x1, X[:, 2:]]
        elif dataset_name == "SA":
            idx = rng.choice(X.shape[0], int(X.shape[0] * 0.1), replace=False)
            X = X[idx]  # Stichprobengröße reduzieren
            y = y[idx]
            x1 = lb.fit_transform(X[:, 1].astype(str))
            x2 = lb.fit_transform(X[:, 2].astype(str))
            x3 = lb.fit_transform(X[:, 3].astype(str))
            X = np.c_[X[:, :1], x1, x2, x3, X[:, 4:]]
        y = (y!= b"normal.").astype(int)
    if dataset_name == "forestcover":
        dataset = fetch_covtype()
        X = dataset.data
        y = dataset.target
        idx = rng.choice(X.shape[0], int(X.shape[0] * 0.1), replace=False)
        X = X[idx]  # Stichprobengröße reduzieren
        y = y[idx]

        # Inlier sind die mit Attribut 2
        # Ausreißer sind die mit Attribut 4
        s = (y == 2) + (y == 4)
        X = X[s, :]
        y = y[s]
        y = (y!= 2).astype(int)
    if dataset_name in ["glass", "wdbc", "cardiotocography"]:
        dataset = fetch_openml(
            name=dataset_name, version=1, as_frame=False, parser="pandas"
        )
        X = dataset.data
        y = dataset.target

        if dataset_name == "glass":
            s = y == "tableware"
            y = s.astype(int)
        if dataset_name == "wdbc":
            s = y == "2"
            y = s.astype(int)
            X_mal, y_mal = X[s], y[s]
            X_ben, y_ben = X[~s], y[~s]

            # auf 39 Punkte abgesampelt (9,8% Ausreißer)
            idx = rng.choice(y_mal.shape[0], 39, replace=False)
            X_mal2 = X_mal[idx]
            y_mal2 = y_mal[idx]
            X = np.concatenate((X_ben, X_mal2), axis=0)
            y = np.concatenate((y_ben, y_mal2), axis=0)
        if dataset_name == "cardiotocography":
            s = y == "3"
            y = s.astype(int)
    # 0 repräsentiert Inlier, und 1 repräsentiert Ausreißer
    y = pd.Series(y, dtype="category")
    return (X, y)
```
