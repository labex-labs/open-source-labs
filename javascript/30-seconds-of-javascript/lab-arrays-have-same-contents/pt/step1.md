# Verificando se Arrays Possuem o Mesmo Conteúdo

Para verificar se dois arrays contêm os mesmos elementos, independentemente da ordem, siga estes passos:

1. Abra o Terminal/SSH e digite `node`.
2. Use um loop `for...of` sobre um `Set` criado a partir dos valores de ambos os arrays.
3. Use `Array.prototype.filter()` para comparar a quantidade de ocorrências de cada valor distinto em ambos os arrays.
4. Retorne `false` se as contagens não corresponderem para nenhum elemento, `true` caso contrário.

Aqui está o código para isso:

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

Para testar a função, use o seguinte código:

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
