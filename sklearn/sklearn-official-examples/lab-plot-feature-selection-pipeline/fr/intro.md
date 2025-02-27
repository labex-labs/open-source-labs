# Introduction

En machine learning, un pipeline est une série d'étapes effectuées séquentiellement pour transformer les données d'entrée puis construire un modèle. Scikit-learn fournit une classe pipeline qui peut être utilisée pour chaîner plusieurs étapes de traitement ensemble, facilitant la construction de modèles complexes impliquant plusieurs étapes de prétraitement et de modélisation.

Dans ce tutoriel, nous allons démontrer comment construire un pipeline avec une sélection de caractéristiques et une classification SVM à l'aide de Scikit-learn. Nous montrerons comment intégrer la sélection de caractéristiques dans le pipeline pour éviter le surapprentissage, et comment examiner le pipeline pour mieux comprendre le modèle.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous réglerons rapidement le problème pour vous.
