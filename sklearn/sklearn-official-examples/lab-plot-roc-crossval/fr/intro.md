# Introduction

Dans ce laboratoire, nous allons apprendre à estimer et à visualiser la variance de la métrique Receiver Operating Characteristic (ROC) à l'aide de la validation croisée en Python. Les courbes ROC sont utilisées dans la classification binaire pour mesurer les performances d'un modèle en traçant le taux de vrais positifs (TPR) en fonction du taux de faux positifs (FPR). Nous utiliserons la bibliothèque Scikit-learn pour charger l'ensemble de données iris, créer des caractéristiques bruitées et classifier l'ensemble de données avec un Support Vector Machine (SVM). Nous tracerons ensuite les courbes ROC avec la validation croisée et calculerons la moyenne de l'aire sous la courbe (AUC) pour voir la variabilité de la sortie du classifieur lorsque l'ensemble d'entraînement est divisé en différents sous-ensembles.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
