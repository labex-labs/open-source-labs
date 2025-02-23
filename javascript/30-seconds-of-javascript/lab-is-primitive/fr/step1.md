# Vérification des valeurs primitives

Pour pratiquer la programmation, ouvrez le Terminal ou SSH et tapez `node`. Une fois que vous avez fait cela, vous pouvez vérifier si une valeur est primitive ou non en suivant ces étapes :

1. Créez un objet à partir de la valeur que vous voulez vérifier en utilisant `Object(val)`.
2. Comparez l'objet créé avec la valeur d'origine à l'aide de l'opérateur d'inégalité stricte `!==`.
3. Si les deux valeurs ne sont pas égales, la valeur d'origine est primitive.

Voici le code de la fonction `isPrimitive` :

```js
const isPrimitive = (val) => Object(val) !== val;
```

Vous pouvez tester cette fonction avec les valeurs suivantes :

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

Si la valeur que vous voulez vérifier est primitive, la fonction renverra `true`. Sinon, elle renverra `false`.
