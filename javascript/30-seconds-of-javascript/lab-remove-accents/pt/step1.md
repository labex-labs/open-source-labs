# Remover Acentos

Esta função remove acentos de strings.

- Use `String.prototype.normalize()` para converter a string para um formato Unicode normalizado.
- Use `String.prototype.replace()` para substituir as marcas diacríticas no intervalo Unicode fornecido por strings vazias.

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

Para usar esta função, abra o Terminal/SSH e digite `node`. Em seguida, chame a função com uma string como seu argumento.

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
