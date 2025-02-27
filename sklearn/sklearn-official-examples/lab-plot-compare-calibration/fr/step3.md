# Interpréter les courbes d'étalonnage

Les courbes d'étalonnage montrent la relation entre les probabilités prédites et les résultats réels pour chaque modèle. Les modèles bien étalonnés produisent des courbes qui suivent la ligne diagonale, indiquant que les probabilités prédites correspondent aux résultats réels. Les quatre modèles produisent des résultats différents :

- La régression logistique produit des prédictions bien étalonnées car elle optimise directement la perte logarithmique.
- Le Bayes Naïf Gaussien a tendance à pousser les probabilités vers 0 ou 1, principalement parce que l'équation du Bayes naïf ne fournit une estimation correcte des probabilités que lorsque l'hypothèse selon laquelle les caractéristiques sont indépendantes conditionnellement est vérifiée.
- Le Classifieur Forestier Aléatoire montre un comportement opposé : les histogrammes montrent des pics à environ 0,2 et 0,9 de probabilité, tandis que les probabilités proches de 0 ou 1 sont très rares.
- Le SVM Linéaire montre une courbe encore plus sigmoïde que le Classifieur Forestier Aléatoire, ce qui est typique des méthodes à marge maximale.
