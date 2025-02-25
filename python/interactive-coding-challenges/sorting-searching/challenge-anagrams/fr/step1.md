# Anagrammes

## Problème

Étant donné un tableau de chaînes de caractères, écrire une fonction pour trier le tableau de sorte que tous les anagrammes soient les uns à côté des autres. Un anagramme est défini comme un mot ou une phrase formée en réarrangeant les lettres d'un autre mot ou phrase. Par exemple, "act" et "cat" sont des anagrammes l'un de l'autre.

## Exigences

Pour résoudre ce problème, les exigences suivantes doivent être satisfaites :

- La fonction doit regrouper tous les anagrammes ensemble dans le tableau trié.
- Il n'y a pas d'autres exigences de tri autres que le regroupement des anagrammes.
- Les entrées peuvent ne pas être valides, donc la fonction doit gérer les entrées invalides.
- La fonction doit tenir en mémoire.

## Utilisation de l'exemple

La fonction devrait se comporter comme suit dans ces scénarios :

- Aucune -> Exception
- [] -> []
- Cas général
  - Entrée : ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
  - Résultat : ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
