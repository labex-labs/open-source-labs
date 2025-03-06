# Mise en majuscule de chaque mot

Maintenant que nous pouvons diviser une chaîne de caractères en mots, nous devons mettre en majuscule la première lettre de chaque mot et les autres lettres en minuscules. Implémentons cette fonctionnalité.

1. Dans votre session Node.js, écrivons une fonction pour mettre en majuscule un seul mot. Tapez :

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

La sortie devrait être :

```
Hello
World
Javascript
```

2. Maintenant, appliquons cette fonction à un tableau de mots en utilisant la méthode `map()`. Tapez :

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

La sortie devrait être :

```
[ 'Hello', 'World', 'Javascript' ]
```

La méthode `map()` crée un nouveau tableau en appliquant une fonction à chaque élément du tableau original. Dans ce cas, nous appliquons notre fonction `capitalizeWord` à chaque mot.

3. Enfin, joignons les mots mis en majuscule pour former une chaîne de caractères en casse Pascal (Pascal case) :

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

La sortie devrait être :

```
HelloWorldJavascript
```

La méthode `join("")` combine tous les éléments d'un tableau en une seule chaîne de caractères, en utilisant le délimiteur fourni (une chaîne vide dans ce cas) entre chaque élément.

Ces étapes démontrent le processus essentiel de conversion d'une chaîne de caractères en casse Pascal :

1. Diviser la chaîne de caractères en mots
2. Mettre en majuscule chaque mot
3. Joindre les mots sans aucun séparateur
