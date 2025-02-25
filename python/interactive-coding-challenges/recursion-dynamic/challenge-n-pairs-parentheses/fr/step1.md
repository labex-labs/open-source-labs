# N paires de parenthèses

## Problème

Le problème consiste à trouver toutes les combinaisons valides de n paires de parenthèses. Une combinaison valide est une combinaison dans laquelle chaque parenthèse ouvrante a une parenthèse fermante correspondante et les paires de parenthèses sont correctement imbriquées. Par exemple, les combinaisons suivantes sont des combinaisons valides de 3 paires de parenthèses :

- ((()))
- (()())
- (())()
- ()(())
- ()()()

Les combinaisons suivantes ne sont pas des combinaisons valides de 3 paires de parenthèses :

- )()(
- ((()
- ))((
- ()()()

## Exigences

Pour résoudre ce problème, nous devons répondre aux questions suivantes :

- L'entrée est-elle un entier représentant le nombre de paires?
  - Oui, l'entrée est un entier représentant le nombre de paires.
- Peut-on supposer que les entrées sont valides?
  - Non, nous ne pouvons pas supposer que les entrées sont valides.
- La sortie est-elle une liste de combinaisons valides?
  - Oui, la sortie est une liste de combinaisons valides.
- La sortie doit-elle avoir des doublons?
  - Non, la sortie ne doit pas avoir de doublons.
- Peut-on supposer que cela tient en mémoire?
  - Oui, nous pouvons supposer que cela tient en mémoire.

## Utilisation de l'exemple

Voici des exemples d'utilisation de la fonction :

- None -> Exception
- Négatif -> Exception
- 0 -> []
- 1 -> ['()']
- 2 -> ['(())', '()()']
- 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
