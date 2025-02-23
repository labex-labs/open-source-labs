# Comment générer une valeur booléenne aléatoire en JavaScript

Pour générer une valeur booléenne aléatoire en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Math.random()` pour générer un nombre aléatoire.
3. Vérifiez si le nombre aléatoire est supérieur ou égal à `0,5`.
4. Retournez `true` si le nombre est supérieur ou égal à `0,5`, sinon retournez `false`.

Voici une implémentation concise du code :

```js
const randomBoolean = () => Math.random() >= 0.5;
```

Vous pouvez tester la fonction en appelant `randomBoolean()` qui retournera soit `true` soit `false`.
