# Introduction

Ce laboratoire présente le tri en cas d'égalité dans les SVM et son impact sur la frontière de décision. En SVM, le tri en cas d'égalité est le mécanisme utilisé pour résoudre les conflits entre deux ou plusieurs classes lorsque leurs distances sont égales. Il n'est pas activé par défaut lorsque `decision_function_shape='ovr'` car cela est coûteux. Par conséquent, ce laboratoire illustre l'effet du paramètre `break_ties` pour un problème de classification multiclasse avec `decision_function_shape='ovr'`.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session et nous réglerons rapidement le problème pour vous.
