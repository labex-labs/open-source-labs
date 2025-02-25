# Trie

## Problème

Votre tâche est d'implémenter un trie avec les méthodes suivantes :

- `trouver(mot)` - renvoie `Vrai` si le mot donné est dans le trie, `Faux` sinon.
- `insérer(mot)` - insère le mot donné dans le trie.
- `supprimer(mot)` - supprime le mot donné du trie.
- `lister_mots()` - renvoie une liste de tous les mots dans le trie qui se terminent par un caractère de terminaison.

## Exigences

Pour résoudre ce défi, les exigences suivantes doivent être satisfaites :

- L'implémentation doit fonctionner avec des chaînes de caractères.
- Les chaînes de caractères sont supposées être en ASCII.
- La méthode `trouver` ne doit correspondre qu'à des mots exacts avec un caractère de terminaison.
- La méthode `lister_mots` ne doit renvoyer que des mots avec un caractère de terminaison.
- Il est supposé que l'implémentation rentre en mémoire.

## Utilisation de l'exemple

Les exemples suivants démontrent l'utilisation des méthodes du trie :

```txt

         racine
       /  |  \
      h   a*  m
     / \   \   \
    a   e*  t*  e*
   / \         / \
  s*  t*      n*  t*
             /
            s*

trouver

* Rechercher dans un trie vide
* Rechercher sans correspondance
* Rechercher avec correspondance

insérer

* Insérer dans un trie vide
* Insérer pour créer un terminateur de feuille
* Insérer pour étendre un terminateur de feuille existant

supprimer

* Supprimer moi
* Supprimer mens
* Supprimer a
* Supprimer has

lister_mots

* Lister vide
* Lister cas général
```
