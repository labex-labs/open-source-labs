# Introduction

Les hyperparamètres sont des paramètres qui ne sont pas directement appris par un estimateur. Ils sont passés en tant qu'arguments au constructeur des classes d'estimateur. Le réglage des hyperparamètres d'un estimateur est une étape importante dans la construction de modèles d'apprentissage automatique performants. Cela consiste à trouver la combinaison optimale d'hyperparamètres qui conduit à la meilleure performance du modèle.

Scikit-learn fournit plusieurs outils pour rechercher les meilleurs hyperparamètres : `GridSearchCV` et `RandomizedSearchCV`. Dans ce laboratoire, nous allons parcourir le processus de réglage des hyperparamètres à l'aide de ces outils.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous réglerons rapidement le problème pour vous.
