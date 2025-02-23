# Comment générer un nombre aléatoire dans une plage donnée à l'aide de JavaScript

Pour générer un nombre aléatoire dans une plage spécifiée à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Math.random()` pour générer une valeur aléatoire.
3. Map la valeur générée dans la plage souhaitée en utilisant la multiplication.
4. Utilisez le code suivant pour créer une fonction qui génère un nombre aléatoire dans la plage donnée :

```js
const randomNumberInRange = (min, max) => Math.random() * (max - min) + min;
```

5. Pour utiliser la fonction, passez les valeurs minimales et maximales de la plage souhaitée en arguments. Par exemple :

```js
randomNumberInRange(2, 10); // 6.0211363285087005
```

En suivant ces étapes, vous pouvez facilement générer un nombre aléatoire dans une plage donnée à l'aide de JavaScript.
