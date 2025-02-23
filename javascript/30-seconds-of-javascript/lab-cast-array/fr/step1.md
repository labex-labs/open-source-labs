# Convertir des valeurs en tableaux en JavaScript

Pour convertir une valeur en tableau, utilisez la fonction `castArray` ci-dessous.

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

Pour utiliser cette fonction, passez en argument la valeur que vous voulez convertir. La fonction vérifiera si la valeur est déjà un tableau en utilisant `Array.isArray()`. Si c'est un tableau, la fonction le renverra tel quel. Si ce n'est pas un tableau, la fonction renverra la valeur encapsulée dans un tableau.

Voici un exemple de manière d'utiliser `castArray` :

```js
castArray("foo"); // renvoie : ['foo']
castArray([1]); // renvoie : [1]
```

Pour commencer à pratiquer la programmation en JavaScript, ouvrez le Terminal ou SSH et tapez `node`.
