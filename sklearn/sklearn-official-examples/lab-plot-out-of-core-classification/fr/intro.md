# Introduction

Ce laboratoire fournit un exemple sur la manière d'utiliser scikit-learn pour la classification de texte en utilisant l'apprentissage hors mémoire. L'objectif est d'apprendre à partir de données qui ne rentrent pas en mémoire principale. Pour y arriver, nous utilisons un classifieur en ligne qui prend en charge la méthode partial_fit, qui sera alimenté avec des lots d'exemples. Pour s'assurer que l'espace de caractéristiques reste le même au fil du temps, nous utilisons un HashingVectorizer qui projettera chaque exemple dans le même espace de caractéristiques. Cela est particulièrement utile dans le cas de la classification de texte où de nouvelles caractéristiques (mots) peuvent apparaître dans chaque lot.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
