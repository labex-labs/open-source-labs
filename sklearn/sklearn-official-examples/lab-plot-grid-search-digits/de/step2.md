# Grid-Search-Strategie definieren

Wir werden eine Funktion definieren, die an den `refit`-Parameter der `GridSearchCV`-Instanz übergeben wird. Sie wird die benutzerdefinierte Strategie implementieren, um den besten Kandidaten aus dem `cv_results_`-Attribut der `GridSearchCV` auszuwählen. Nachdem der Kandidat ausgewählt ist, wird er automatisch von der `GridSearchCV`-Instanz erneut trainiert.

Hierbei ist die Strategie, die Modelle aufzulisten, die in Bezug auf Präzision und Recall die besten sind. Aus den ausgewählten Modellen wählen wir schließlich das am schnellsten vorhersagende Modell. Beachten Sie, dass diese benutzerdefinierten Auswahlkriterien völlig willkürlich sind.

```python
import pandas as pd
from sklearn.metrics import classification_report

def print_dataframe(filtered_cv_results):
    """Schönformatiertes Ausgeben eines gefilterten DataFrames"""
    for mean_precision, std_precision, mean_recall, std_recall, params in zip(
        filtered_cv_results["mean_test_precision"],
        filtered_cv_results["std_test_precision"],
        filtered_cv_results["mean_test_recall"],
        filtered_cv_results["std_test_recall"],
        filtered_cv_results["params"],
    ):
        print(
            f"Präzision: {mean_precision:0.3f} (±{std_precision:0.03f}),"
            f" Recall: {mean_recall:0.3f} (±{std_recall:0.03f}),"
            f" für {params}"
        )
    print()


def refit_strategy(cv_results):
    """Definiert die Strategie, um den besten Schätzer auszuwählen.

    Die hier definierte Strategie besteht darin, alle Ergebnisse unter einem Präzisionsschwellenwert
    von 0.98 auszuschließen, die verbleibenden nach Recall zu rangieren und alle Modelle mit einer
    Standardabweichung des besten nach Recall zu behalten. Nachdem diese Modelle ausgewählt sind,
    können wir das am schnellsten vorhersagende Modell auswählen.

    Parameter
    ----------
    cv_results : dict von numpy (maskierten) ndarrays
        CV-Ergebnisse, wie sie von der `GridSearchCV` zurückgegeben werden.

    Rückgabewert
    -------
    best_index : int
        Der Index des besten Schätzers, wie er in `cv_results` erscheint.
    """
    # Druckt die Informationen zur Grid-Search für die verschiedenen Scores
    precision_threshold = 0.98

    cv_results_ = pd.DataFrame(cv_results)
    print("Alle Grid-Search-Ergebnisse:")
    print_dataframe(cv_results_)

    # Filtert alle Ergebnisse unterhalb der Schwelle aus
    high_precision_cv_results = cv_results_[
        cv_results_["mean_test_precision"] > precision_threshold
    ]

    print(f"Modelle mit einer Präzision höher als {precision_threshold}:")
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

    # Wählt die leistungsfähigsten Modelle in Bezug auf Recall aus
    # (innerhalb von 1 Sigma vom besten)
    best_recall_std = high_precision_cv_results["mean_test_recall"].std()
    best_recall = high_precision_cv_results["mean_test_recall"].max()
    best_recall_threshold = best_recall - best_recall_std

    high_recall_cv_results = high_precision_cv_results[
        high_precision_cv_results["mean_test_recall"] > best_recall_threshold
    ]
    print(
        "Von den zuvor ausgewählten Modellen mit hoher Präzision behalten wir alle\n"
        "die Modelle innerhalb einer Standardabweichung des Modells mit der höchsten Recall:\n"
    )
    print_dataframe(high_recall_cv_results)

    # Aus den besten Kandidaten wählt das am schnellsten vorhersagende Modell aus
    fastest_top_recall_high_precision_index = high_recall_cv_results[
        "mean_score_time"
    ].idxmin()

    print(
        "\nDas ausgewählte finale Modell ist das am schnellsten vorhersagende aus der zuvor\n"
        "ausgewählten Teilmenge der besten Modelle basierend auf Präzision und Recall.\n"
        "Seine Bewertungszeit ist:\n\n"
        f"{high_recall_cv_results.loc[fastest_top_recall_high_precision_index]}"
    )

    return fastest_top_recall_high_precision_index
```
