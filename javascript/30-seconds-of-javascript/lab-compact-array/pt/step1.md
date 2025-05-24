# Como Usar Array.prototype.filter() para Criar um Array Compacto

Para criar um array compacto em JavaScript, você pode usar o método `Array.prototype.filter()` para remover quaisquer valores falsos (falsy values) do array. Valores falsos incluem `false`, `null`, `0`, `""`, `undefined` e `NaN`.

Aqui está um trecho de código de exemplo que demonstra como criar um array compacto usando `Array.prototype.filter()`:

```js
const compact = (arr) => arr.filter(Boolean);
```

Você pode então usar a função `compact` para criar um array compacto, passando um array como argumento. Por exemplo:

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// Output: [ 1, 2, 3, 'a', 's', 34 ]
```

Ao usar `Array.prototype.filter()` dessa forma, você pode facilmente criar um array compacto que contém apenas valores verdadeiros (truthy values).
