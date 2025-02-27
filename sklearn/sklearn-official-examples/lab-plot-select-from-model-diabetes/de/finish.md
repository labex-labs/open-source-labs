# Zusammenfassung

In diesem Lab wurden zwei Ansätze zur Featureauswahl demonstriert: modellbasiert und sequentielle Featureauswahl. Wir haben den RidgeCV-Schätzer verwendet, um die Wichtigkeit der Features zu bestimmen, und SelectFromModel, um Features basierend auf ihrer Wichtigkeit auszuwählen. Der Sequential Feature Selector ist ein greedy-Verfahren, bei dem wir in jeder Iteration das beste neue Feature auswählen, das wir zu unseren ausgewählten Features hinzufügen möchten, basierend auf einem Kreuzvalidierungsscore.
