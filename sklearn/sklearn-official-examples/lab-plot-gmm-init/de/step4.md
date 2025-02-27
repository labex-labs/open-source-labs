# Die Ergebnisse interpretieren

Wir können aus dem Diagramm sehen, dass `k-means++` sowohl eine geringe Initialisierungszeit als auch eine geringe Anzahl an Iterationen des GaussianMixture benötigt, um sich zu konvergieren. Wenn mit `random_from_data` oder `random` initialisiert wird, benötigt das Modell mehr Iterationen, um sich zu konvergieren. Alle drei alternativen Methoden benötigen weniger Zeit zur Initialisierung im Vergleich zu `kmeans`.
