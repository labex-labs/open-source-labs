# Comment créer un clone superficiel d'un objet

Pour créer un clone superficiel d'un objet, utilisez `Object.assign()` et un objet vide (`{}`). Suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le code suivant pour créer un clone superficiel de l'objet original :

```js
const shallowClone = (obj) => Object.assign({}, obj);
```

3. Pour cloner l'objet, utilisez la fonction `shallowClone()` comme suit :

```js
const a = { x: true, y: 1 };
const b = shallowClone(a); // a!== b
```

Dans cet exemple, `a` et `b` sont deux objets différents, mais ils ont les mêmes valeurs.
