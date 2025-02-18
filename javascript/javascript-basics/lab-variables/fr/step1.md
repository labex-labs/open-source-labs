# Variables

> Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

Les variables sont des conteneurs qui stockent des valeurs. Vous commencez par déclarer une variable avec le mot-clé `let`, suivi du nom que vous donnez à la variable :

```js
let myVariable;
```

Un point-virgule à la fin d'une ligne indique où une instruction se termine. Il est uniquement requis lorsque vous devez séparer des instructions sur une seule ligne. Cependant, certaines personnes pensent qu'il est bon de mettre des points-virgules à la fin de chaque instruction. Il existe d'autres règles concernant l'utilisation ou non des points-virgules.

Vous pouvez nommer une variable presque comme vous le souhaitez, mais il y a quelques restrictions. Si vous n'êtes pas sûr, vous pouvez [vérifier le nom de votre variable](https://mothereff.in/js-variables) pour voir s'il est valide.

JavaScript est sensible à la casse. Cela signifie que `myVariable` n'est pas le même que `myvariable`. Si vous rencontrez des problèmes dans votre code, vérifiez la casse!

Après avoir déclaré une variable, vous pouvez lui attribuer une valeur :

```js
myVariable = "Bob";
```

De plus, vous pouvez effectuer ces deux opérations sur la même ligne :

```js
let myVariable = "Bob";
```

Vous récupérez la valeur en appelant le nom de la variable :

```js
myVariable;
```

Après avoir attribué une valeur à une variable, vous pouvez la changer plus tard dans le code :

```js
let myVariable = "Bob";
myVariable = "Steve";
```

Notez que les variables peuvent contenir des valeurs de différents [types de données](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures) :

| Variable                                                                                  | Explication                                                                                                                                                             | Exemple                                                                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Chaîne de caractères (String)](https://developer.mozilla.org/en-US/docs/Glossary/String) | Il s'agit d'une séquence de texte appelée chaîne de caractères. Pour indiquer que la valeur est une chaîne de caractères, entourez-la de guillemets simples ou doubles. | `let myVariable = 'Bob';` ou `let myVariable = "Bob";`                                                                                    |
| [Nombre (Number)](https://developer.mozilla.org/en-US/docs/Glossary/Number)               | Il s'agit d'un nombre. Les nombres ne sont pas entourés de guillemets.                                                                                                  | `let myVariable = 10;`                                                                                                                    |
| [Booléen (Boolean)](https://developer.mozilla.org/en-US/docs/Glossary/Boolean)            | Il s'agit d'une valeur Vrai/Faux. Les mots `true` et `false` sont des mots-clés spéciaux qui n'ont pas besoin de guillemets.                                            | `let myVariable = true;`                                                                                                                  |
| [Tableau (Array)](https://developer.mozilla.org/en-US/docs/Glossary/Array)                | Il s'agit d'une structure qui vous permet de stocker plusieurs valeurs dans une seule référence.                                                                        | `let myVariable = [1,'Bob','Steve',10];` Faites référence à chaque élément du tableau comme ceci : `myVariable[0]`, `myVariable[1]`, etc. |
| [Objet (Object)](https://developer.mozilla.org/en-US/docs/Glossary/Object)                | Cela peut être n'importe quoi. Tout en JavaScript est un objet et peut être stocké dans une variable. Gardez cela à l'esprit tout au long de votre apprentissage.       | `let myVariable = document.querySelector('h1');` Tous les exemples ci-dessus aussi.                                                       |

Alors, pourquoi avons-nous besoin de variables? Les variables sont nécessaires pour faire tout ce qui est intéressant en programmation. Si les valeurs ne pouvaient pas changer, vous ne pourriez rien faire de dynamique, comme personnaliser un message de salutation ou changer une image affichée dans une galerie d'images.
