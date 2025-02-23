# Résumé

Supprimer les branches détachées est une étape importante pour maintenir votre référentiel Git organisé et facile à gérer. En utilisant la commande `git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D`, vous pouvez facilement supprimer toutes les branches détachées de votre référentiel local. Cela vous aidera à conserver votre référentiel propre et à le rendre plus pratique à utiliser à l'avenir.
