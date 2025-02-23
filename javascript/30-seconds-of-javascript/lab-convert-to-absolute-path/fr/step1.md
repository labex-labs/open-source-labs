# Comment convertir un chemin avec le tilde en chemin absolu dans Node.js

Pour commencer à pratiquer le codage dans Node.js, ouvrez le Terminal ou SSH et tapez `node`. Pour convertir un chemin avec le tilde en chemin absolu, utilisez le code suivant :

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

Le code utilise `String.prototype.replace()` avec une expression régulière et `os.homedir()` pour remplacer le `~` au début du chemin par le répertoire personnel. Voici un exemple d'utilisation de la fonction `untildify` :

```js
untildify("~/node"); // renvoie '/Users/aUser/node'
```
