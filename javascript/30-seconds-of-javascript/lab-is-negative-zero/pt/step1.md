# Verificando Zero Negativo

Para verificar se um número é zero negativo, abra o Terminal/SSH e digite `node`. Em seguida, use o seguinte código:

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

Isso verificará se o valor passado é igual a `0` e se `1` dividido pelo valor é igual a `-Infinity`. Por exemplo:

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
