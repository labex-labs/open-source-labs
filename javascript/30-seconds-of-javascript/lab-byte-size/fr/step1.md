# Comprendre la représentation des chaînes de caractères (strings) en JavaScript

Avant de calculer la taille en octets des chaînes de caractères, il est important de comprendre comment les chaînes de caractères sont représentées en JavaScript.

En JavaScript, les chaînes de caractères sont des séquences d'unités de code UTF - 16. Cela signifie que des caractères tels que les emojis ou certains symboles peuvent nécessiter plus d'un octet pour être représentés. Par exemple, une simple lettre anglaise prend 1 octet, mais un emoji peut prendre 4 octets.

Commençons par lancer Node.js dans le terminal :

1. Ouvrez le terminal en cliquant sur l'icône du terminal dans l'interface WebIDE.
2. Tapez la commande suivante et appuyez sur Entrée :

```bash
node
```

Vous devriez maintenant être dans la console interactive Node.js, qui ressemble à quelque chose comme ceci :

```
Welcome to Node.js v14.x.x.
Type ".help" for more information.
>
```

![Ouvrir Node](../assets/screenshot-20250306-cFJ9GgLX@2x.png)

Dans cette console, nous pouvons tester directement du code JavaScript. Essayez de taper la commande suivante pour voir la longueur d'une chaîne de caractères :

```javascript
"Hello World".length;
```

Vous devriez voir le résultat suivant :

```
11
```

Cela nous donne le nombre de caractères, mais pas la taille réelle en octets. Le nombre de caractères et la taille en octets peuvent être différents, en particulier avec des caractères spéciaux. Explorons cela plus en détail à l'étape suivante.
