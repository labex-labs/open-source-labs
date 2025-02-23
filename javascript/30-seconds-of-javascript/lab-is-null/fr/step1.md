# Vérification si une valeur est nulle

Pour vérifier si une valeur est `null` en JavaScript, utilisez l'opérateur d'égalité stricte (`===`). Voici un extrait de code d'exemple qui définit une fonction appelée `isNull` qui renvoie `true` si la valeur donnée est `null` et `false` dans le cas contraire.

```js
const isNull = (val) => val === null;
```

Pour tester cette fonction, vous pouvez l'appeler avec la valeur que vous voulez vérifier en tant qu'argument. Par exemple, `isNull(null)` renverra `true`.
