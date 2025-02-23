# Deep Map Object Keys

Pour mapper de manière récursive les clés d'un objet, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `deepMapKeys` avec l'objet fourni et une fonction qui génère de nouvelles clés.
3. La fonction crée un objet avec les mêmes valeurs que l'objet fourni et des clés générées en exécutant la fonction fournie pour chaque clé.
4. Itérez sur les clés de l'objet à l'aide de `Object.keys()`.
5. Créez un nouvel objet avec les mêmes valeurs et les clés mappées à l'aide de `Array.prototype.reduce()` et de la fonction fournie.
6. Si une valeur est un objet, appelez `deepMapKeys` de manière récursive sur elle pour mapper également ses clés.

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

Voici un exemple d'utilisation de `deepMapKeys` :

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
