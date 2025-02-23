# Fonction pour lier une méthode d'objet

Pour créer une fonction qui lie une méthode d'objet à son contexte et optionnellement ajoute des paramètres supplémentaires au début, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Définissez une fonction qui prend trois paramètres : le contexte de l'objet, la clé de la méthode et tous les arguments supplémentaires à ajouter au début.
3. La fonction devrait renvoyer une nouvelle fonction qui utilise `Function.prototype.apply()` pour lier la méthode au contexte de l'objet.
4. Utilisez l'opérateur de propagation (`...`) pour ajouter tous les paramètres supplémentaires fournis aux arguments.
5. Voici une implémentation exemple :

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6. Pour tester la fonction, créez un objet avec une méthode et liez-la à l'aide de `bindKey()`. Ensuite, appelez la méthode liée avec quelques arguments.

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  }
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
