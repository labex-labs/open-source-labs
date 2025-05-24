# Aqui está uma dica sobre como Compactar e Juntar um Array

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Veja como remover valores falsos de um array e combinar os valores restantes em uma string:

- Use `Array.prototype.filter()` para filtrar valores falsos como `false`, `null`, `0`, `""`, `undefined` e `NaN`.
- Use `Array.prototype.join()` para juntar os valores restantes em uma string.

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

Em seguida, chame a função e passe um array como argumento:

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
