# Native Unterstützung von kategorischen Merkmalen

In diesem Abschnitt bauen und evaluieren wir eine Pipeline, die die native Unterstützung von kategorischen Merkmalen in `HistGradientBoostingRegressor` verwendet, das nur bis zu 255 eindeutige Kategorien unterstützt. Wir gruppieren die kategorischen Merkmale in Merkmale mit geringer Kardinalität und Merkmale mit hoher Kardinalität. Die Merkmale mit hoher Kardinalität werden Zielkodiert, und die Merkmale mit geringer Kardinalität werden die native kategorische Funktion in Gradient Boosting verwenden.
