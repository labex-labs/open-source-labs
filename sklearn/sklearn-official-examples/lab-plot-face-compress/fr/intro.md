# Introduction

Ce laboratoire montre comment utiliser KBinsDiscretizer de la bibliothèque Scikit-learn pour effectuer une quantification vectorielle sur une image d'échantillon du visage d'un raton laveur. La quantification vectorielle est une technique pour réduire le nombre de niveaux de gris utilisés pour représenter une image. Nous utiliserons KBinsDiscretizer pour effectuer une quantification vectorielle sur l'image du visage du raton laveur. Nous utiliserons 8 niveaux de gris pour représenter l'image, ce qui peut être compressé pour n'utiliser que 3 bits par pixel. Nous comparerons les stratégies d'échantillonnage uniforme et de regroupement k-moyennes pour mapper les valeurs de pixel aux 8 niveaux de gris.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous résoudrons rapidement le problème pour vous.
