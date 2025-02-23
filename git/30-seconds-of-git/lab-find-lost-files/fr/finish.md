# Résumé

Utiliser Git pour trouver des fichiers perdus et des commits peut être un sauvetage lorsqu'on travaille sur un projet. En exécutant la commande `git fsck --lost-found`, vous pouvez identifier tout objet orphelin et l'extraire dans le répertoire `.git/lost-found`. À partir de là, vous pouvez examiner les fichiers pour déterminer s'ils sont les fichiers manquants.
