# Comment vérifier si une date est postérieure à une autre date en JavaScript

Pour vérifier si une date est postérieure à une autre date en JavaScript, vous pouvez utiliser l'opérateur supérieur (`>`). Voici un extrait de code d'exemple qui vérifie si une date donnée (`dateA`) est postérieure à une autre date (`dateB`):

```js
const isAfterDate = (dateA, dateB) => dateA > dateB;
```

Pour utiliser cette fonction, il suffit de passer deux objets de date, comme ceci :

```js
isAfterDate(new Date(2010, 10, 21), new Date(2010, 10, 20)); // true
```

Pour tester cela, vous pouvez ouvrir le Terminal/SSH et taper `node` pour commencer à pratiquer la programmation.
