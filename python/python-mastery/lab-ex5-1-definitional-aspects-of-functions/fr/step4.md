# Défi de conception : Entêtes CSV

Le code suppose que la première ligne des données CSV contient toujours des en-têtes de colonne. Cependant, ce n'est pas toujours le cas. Par exemple, le fichier `portfolio_noheader.csv` contient des données, mais pas d'en-têtes de colonne.

Comment refactoriseriez-vous le code pour prendre en compte l'absence d'en-têtes de colonne, les ayant fournis manuellement par l'appelant à la place?
