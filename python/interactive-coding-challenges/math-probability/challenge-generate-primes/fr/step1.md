# Générer des nombres premiers

## Problème

Écrire une fonction Python qui génère une liste de nombres premiers. La fonction devrait prendre un entier en entrée et renvoyer une liste de valeurs booléennes, où chaque valeur correspond à savoir si l'index est un nombre premier ou non. Par exemple, si l'entrée est 20, la sortie devrait être [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True], où la valeur à l'index 2 est True car 2 est un nombre premier, et la valeur à l'index 4 est False car 4 n'est pas un nombre premier.

## Exigences

- La fonction ne devrait pas considérer 1 comme un nombre premier.
- La fonction devrait gérer les entrées invalides en levant une exception.
- La fonction devrait générer la liste de nombres premiers en mémoire.

## Utilisation exemple

- Aucune valeur -> Exception
- Pas un int -> Exception
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
