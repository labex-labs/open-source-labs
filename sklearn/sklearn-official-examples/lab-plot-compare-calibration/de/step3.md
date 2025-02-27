# Kalibrierungskurven interpretieren

Die Kalibrierungskurven zeigen die Beziehung zwischen vorhergesagten Wahrscheinlichkeiten und tatsächlichen Ergebnissen für jedes Modell. Gut kalibrierte Modelle erzeugen Kurven, die der Diagonalen folgen, was darauf hinweist, dass vorhergesagte Wahrscheinlichkeiten mit tatsächlichen Ergebnissen übereinstimmen. Die vier Modelle ergeben unterschiedliche Ergebnisse:

- Die logistische Regression liefert gut kalibrierte Vorhersagen, da sie direkt das Log-Loss optimiert.
- Der Gaußsche Naiver Bayes tendiert dazu, Wahrscheinlichkeiten auf 0 oder 1 zu drängen, hauptsächlich weil die Gleichung des naiven Bayes nur eine korrekte Schätzung der Wahrscheinlichkeiten liefert, wenn die Annahme der bedingten Unabhängigkeit der Merkmale zutrifft.
- Der Random Forest Classifier zeigt das Gegenteil: Die Histogramme zeigen Spitzen bei einer Wahrscheinlichkeit von ca. 0,2 und 0,9, während Wahrscheinlichkeiten nahe bei 0 oder 1 sehr selten sind.
- Der Lineare SVM zeigt eine noch sigmoidere Kurve als der Random Forest Classifier, was für Maximum-Margin-Methoden typisch ist.
