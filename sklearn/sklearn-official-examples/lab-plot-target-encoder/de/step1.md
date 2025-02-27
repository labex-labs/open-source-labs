# Laden von Daten aus OpenML

Zunächst laden wir den Weintest-Datensatz mit der Funktion `fetch_openml` aus dem Modul `scikit-learn.datasets`. Wir werden nur einen Teil der numerischen und kategorischen Merkmale im Datensatz verwenden. Wir werden die folgenden Teilmengen von numerischen und kategorischen Merkmalen im Datensatz verwenden: `numerische_Merkmale = ["price"]` und `kategorische_Merkmale = ["country", "province", "region_1", "region_2", "variety", "winery"]`.
