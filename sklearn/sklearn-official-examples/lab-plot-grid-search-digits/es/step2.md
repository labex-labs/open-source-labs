# Definir la estrategia de búsqueda en cuadrícula

Definiremos una función que se pasará al parámetro `refit` de la instancia `GridSearchCV`. Implementará la estrategia personalizada para seleccionar el mejor candidato a partir del atributo `cv_results_` de la instancia `GridSearchCV`. Una vez que se ha seleccionado el candidato, se ajusta automáticamente por la instancia `GridSearchCV`.

Aquí, la estrategia es reducir a una lista los modelos que son los mejores en términos de precisión y recuperación. A partir de los modelos seleccionados, finalmente elegimos el modelo más rápido en la predicción. Tenga en cuenta que estas elecciones personalizadas son completamente arbitrarias.

```python
import pandas as pd
from sklearn.metrics import classification_report

def print_dataframe(filtered_cv_results):
    """Impresión bonita para el dataframe filtrado"""
    for mean_precision, std_precision, mean_recall, std_recall, params in zip(
        filtered_cv_results["mean_test_precision"],
        filtered_cv_results["std_test_precision"],
        filtered_cv_results["mean_test_recall"],
        filtered_cv_results["std_test_recall"],
        filtered_cv_results["params"],
    ):
        print(
            f"precision: {mean_precision:0.3f} (±{std_precision:0.03f}),"
            f" recall: {mean_recall:0.3f} (±{std_recall:0.03f}),"
            f" para {params}"
        )
    print()


def refit_strategy(cv_results):
    """Define la estrategia para seleccionar el mejor estimador.

    La estrategia definida aquí es filtrar todos los resultados por debajo de un umbral de precisión
    del 0.98, clasificar los restantes por recuperación y mantener todos los modelos con una
    desviación estándar del mejor por recuperación. Una vez que se han seleccionado estos modelos,
    podemos elegir el modelo más rápido para predecir.

    Parámetros
    ----------
    cv_results : dict de ndarrays de numpy (enmascarados)
        Resultados de la validación cruzada devueltos por el `GridSearchCV`.

    Devuelve
    -------
    best_index : int
        El índice del mejor estimador tal como aparece en `cv_results`.
    """
    # Imprime la información sobre la búsqueda en cuadrícula para las diferentes puntuaciones
    precision_threshold = 0.98

    cv_results_ = pd.DataFrame(cv_results)
    print("Todos los resultados de la búsqueda en cuadrícula:")
    print_dataframe(cv_results_)

    # Filtra todos los resultados por debajo del umbral
    high_precision_cv_results = cv_results_[
        cv_results_["mean_test_precision"] > precision_threshold
    ]

    print(f"Modelos con una precisión mayor que {precision_threshold}:")
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

    # Selecciona los modelos más performantes en términos de recuperación
    # (dentro de 1 sigma del mejor)
    best_recall_std = high_precision_cv_results["mean_test_recall"].std()
    best_recall = high_precision_cv_results["mean_test_recall"].max()
    best_recall_threshold = best_recall - best_recall_std

    high_recall_cv_results = high_precision_cv_results[
        high_precision_cv_results["mean_test_recall"] > best_recall_threshold
    ]
    print(
        "De los modelos de alta precisión previamente seleccionados, mantenemos todos los\n"
        "modelos dentro de una desviación estándar del modelo de mayor recuperación:"
    )
    print_dataframe(high_recall_cv_results)

    # De los mejores candidatos, selecciona el modelo más rápido para predecir
    fastest_top_recall_high_precision_index = high_recall_cv_results[
        "mean_score_time"
    ].idxmin()

    print(
        "\nEl modelo final seleccionado es el más rápido para predecir dentro del\n"
        "subconjunto previamente seleccionado de mejores modelos basados en precisión y recuperación.\n"
        "Su tiempo de puntuación es:\n\n"
        f"{high_recall_cv_results.loc[fastest_top_recall_high_precision_index]}"
    )

    return fastest_top_recall_high_precision_index
```
