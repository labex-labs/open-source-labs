# Sommaire

On sait que le Lasso permet de récupérer efficacement des données creuses, mais ne fonctionne pas bien avec des caractéristiques fortement corrélées. En effet, si plusieurs caractéristiques corrélées contribuent à la variable cible, le Lasso finira par n'en sélectionner qu'une seule. Dans le cas de caractéristiques creuses mais non corrélées, un modèle Lasso serait plus approprié.

ElasticNet introduit une certaine rareté dans les coefficients et les réduit à zéro. Ainsi, en présence de caractéristiques corrélées qui contribuent à la variable cible, le modèle est toujours capable de réduire leurs poids sans les ramener exactement à zéro. Cela conduit à un modèle moins creux qu'un Lasso pur et peut également capturer des caractéristiques non prédictives.

ARDRegression est meilleur lorsqu'il s'agit de gérer un bruit gaussien, mais est toujours incapable de gérer des caractéristiques corrélées et nécessite un temps plus important en raison de l'ajustement d'une a priori.
