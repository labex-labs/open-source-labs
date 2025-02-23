# Clonage d'une expression régulière

Pour cloner une expression régulière, utilisez le constructeur `RegExp`, `RegExp.prototype.source` et `RegExp.prototype.flags`.

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

Ce code créera un clone de l'expression régulière donnée. Par exemple :

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp!== regExp2
```
