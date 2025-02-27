# Introduction

La Régression par Composantes Principales (PCR) et la Régression par Moindres Carrés Partiels (PLS) sont deux méthodes utilisées dans l'analyse de régression. La PCR consiste à appliquer l'Analyse en Composantes Principales (PCA) aux données d'entraînement, puis à entraîner un régresseur sur les échantillons transformés. La transformation PCA est non supervisée, ce qui signifie qu'aucune information sur les cibles n'est utilisée. En conséquence, la PCR peut donner de mauvais résultats dans certains ensembles de données où la cible est fortement corrélée avec des directions ayant une faible variance.

La PLS est à la fois un transformateur et un régresseur, et elle est assez similaire à la PCR. Elle applique également une réduction de dimensionnalité aux échantillons avant d'appliquer un régresseur linéaire aux données transformées. La principale différence avec la PCR est que la transformation PLS est supervisée. Par conséquent, elle ne souffre pas du problème mentionné ci-dessus.

Dans ce laboratoire, nous comparerons la PCR et la PLS sur un ensemble de données de démonstration.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
