# Fonctions

> Le fichier `index.html` a déjà été fourni dans la machine virtuelle.

Les [fonctions](https://developer.mozilla.org/fr/docs/Glossaire/Fonction) sont un moyen de regrouper des fonctionnalités que vous souhaitez réutiliser. Il est possible de définir un bloc de code comme une fonction qui s'exécute lorsque vous appelez le nom de la fonction dans votre code. C'est une bonne alternative au fait d'écrire le même code à plusieurs reprises. Vous avez déjà vu quelques utilisations de fonctions.

Par exemple :

```js
let myVariable = document.querySelector("h1");
```

```js
alert("hello!");
```

Ces fonctions, `document.querySelector` et `alert`, sont intégrées au navigateur.

> Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

Si vous voyez quelque chose qui ressemble à un nom de variable, mais qui est suivi de parenthèses — `()` — il s'agit probablement d'une fonction. Les fonctions prennent souvent des [arguments](https://developer.mozilla.org/fr/docs/Glossaire/Argument) : des morceaux de données dont elles ont besoin pour faire leur travail. Les arguments se placent à l'intérieur des parenthèses, séparés par des virgules s'il y a plusieurs arguments.

Par exemple, la fonction `alert()` fait apparaître une boîte de dialogue dans la fenêtre du navigateur, mais nous devons lui fournir une chaîne de caractères en tant qu'argument pour dire à la fonction quel message afficher.

Vous pouvez également définir vos propres fonctions.

Dans l'exemple suivant, nous créons une fonction simple qui prend deux nombres en arguments et les multiplie :

> Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

```js
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

Essayez d'exécuter ceci dans la console ; puis testez avec plusieurs arguments. Par exemple :

```js
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```

> **Note** : L'instruction [`return`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/return) indique au navigateur de renvoyer la variable `result` en dehors de la fonction afin qu'elle soit disponible pour être utilisée. Cela est nécessaire car les variables définies à l'intérieur de fonctions ne sont disponibles que à l'intérieur de ces fonctions. Cela s'appelle la portée des variables. (Lisez-en plus sur la [portée des variables](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Grammar_and_types#portée_des_variables).)
