# Caractères uniques

## Problème

Étant donné une chaîne de caractères, la tâche consiste à déterminer si elle contient uniquement des caractères uniques. En d'autres termes, il ne devrait pas y avoir de caractères répétés dans la chaîne. Par exemple, la chaîne "hello" ne contient pas uniquement des caractères uniques car la lettre "l" apparaît deux fois. En revanche, la chaîne "world" contient uniquement des caractères uniques car chaque lettre n'apparaît qu'une seule fois.

## Exigences

Pour résoudre ce problème, les exigences suivantes doivent être satisfaites :

- La chaîne est supposée être en ASCII.
  - Les chaînes Unicode peuvent nécessiter une gestion spéciale selon le langage utilisé.
- La casse est supposée être sensible.
- Des structures de données supplémentaires peuvent être utilisées.
- Il est supposé que la chaîne tient en mémoire.

## Utilisation exemple

Voici des exemples de comportement attendu de la fonction :

- None -> False
- '' -> True
- 'foo' -> False
- 'bar' -> True
