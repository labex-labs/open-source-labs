# Définir une stratégie de recherche sur grille

Nous allons définir une fonction à passer au paramètre `refit` de l'instance `GridSearchCV`. Elle implémentera la stratégie personnalisée pour sélectionner le meilleur candidat à partir de l'attribut `cv_results_` de `GridSearchCV`. Une fois le candidat sélectionné, il est automatiquement réajusté par l'instance `GridSearchCV`.

Ici, la stratégie est de sélectionner les modèles qui sont les meilleurs en termes de précision et de rappel. Parmi les modèles sélectionnés, nous sélectionnons finalement le modèle le plus rapide à prédire. Remarquez que ces choix personnalisés sont entièrement arbitraires.

```python
import pandas as pd
from sklearn.metrics import classification_report

def print_dataframe(filtered_cv_results):
    """Affiche joliment un DataFrame filtré"""
    for mean_precision, std_precision, mean_recall, std_recall, params in zip(
        filtered_cv_results["mean_test_precision"],
        filtered_cv_results["std_test_precision"],
        filtered_cv_results["mean_test_recall"],
        filtered_cv_results["std_test_recall"],
        filtered_cv_results["params"],
    ):
        print(
            f"précision: {mean_precision:0.3f} (±{std_precision:0.03f}),"
            f" rappel: {mean_recall:0.3f} (±{std_recall:0.03f}),"
            f" pour {params}"
        )
    print()


def refit_strategy(cv_results):
    """Définit la stratégie pour sélectionner le meilleur estimateur.

    La stratégie définie ici est de filtrer tous les résultats inférieurs à un seuil de précision
    de 0,98, de classer les résultats restants par rappel et de conserver tous les modèles
    avec une écart-type de l'ordre du meilleur modèle en termes de rappel. Une fois ces modèles
    sélectionnés, nous pouvons sélectionner le modèle le plus rapide à prédire.

    Paramètres
    ----------
    cv_results : dict de tableaux ndarray (masqués) de numpy
        Résultats de la validation croisée renvoyés par `GridSearchCV`.

    Retours
    -------
    best_index : int
        L'index du meilleur estimateur tel qu'il apparaît dans `cv_results`.
    """
    # Affiche les informations sur la recherche sur grille pour les différents scores
    precision_threshold = 0,98

    cv_results_ = pd.DataFrame(cv_results)
    print("Tous les résultats de la recherche sur grille :")
    print_dataframe(cv_results_)

    # Filtre tous les résultats inférieurs au seuil
    high_precision_cv_results = cv_results_[
        cv_results_["mean_test_precision"] > precision_threshold
    ]

    print(f"Modèles avec une précision supérieure à {precision_threshold} :")
    print_dataframe(high_precision_cv_results)

    high_precision_cv_results = high_precision_cv_results[
        [
            "mean_score_time",
            "mean_test_recall",
            "std_test_recall",
            "mean_test_precision",
            "std_test_precision",
            "rank_test_recall",
            "rank_test_precision",
            "params",
        ]
    ]

    # Sélectionne les modèles les plus performants en termes de rappel
    # (à l'intérieur d'un écart-type du meilleur)
    best_recall_std = high_precision_cv_results["mean_test_recall"].std()
    best_recall = high_precision_cv_results["mean_test_recall"].max()
    best_recall_threshold = best_recall - best_recall_std

    high_recall_cv_results = high_precision_cv_results[
        high_precision_cv_results["mean_test_recall"] > best_recall_threshold
    ]
    print(
        "Parmi les modèles à haute précision précédemment sélectionnés, nous conservons tous les\n"
        "modèles à l'intérieur d'un écart-type du modèle à rappel le plus élevé : "
    )
    print_dataframe(high_recall_cv_results)

    # Parmi les meilleurs candidats, sélectionne le modèle le plus rapide à prédire
    fastest_top_recall_high_precision_index = high_recall_cv_results[
        "mean_score_time"
    ].idxmin()

    print(
        "\nLe modèle final sélectionné est le plus rapide à prédire parmi les précédemment\n"
        "sélectionnés dans le sous-ensemble de meilleurs modèles basé sur la précision et le rappel.\n"
        "Son temps de scoring est :\n\n"
        f"{high_recall_cv_results.loc[fastest_top_recall_high_precision_index]}"
    )

    return fastest_top_recall_high_precision_index
```
