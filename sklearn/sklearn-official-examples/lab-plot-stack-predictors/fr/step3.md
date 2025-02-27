# Empilement de prédicteurs sur un seul ensemble de données

Maintenant, nous pouvons utiliser le jeu de données Ames Housing pour effectuer les prédictions. Nous vérifions les performances de chaque prédicteur individuel ainsi que celles de la pile de régresseurs. Nous combinons 3 apprenants (linéaires et non linéaires) et utilisons un régresseur ridge pour combiner leurs sorties. Le régresseur empilé combinera les forces des différents régresseurs. Cependant, nous voyons également que l'entraînement du régresseur empilé est beaucoup plus coûteux en termes de calcul.
