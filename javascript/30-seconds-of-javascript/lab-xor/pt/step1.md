# Xor Lógico

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`. O xor lógico verifica se apenas um dos argumentos é `true`. Para criar o xor lógico, use os operadores or lógico (`||`), and (`&&`) e not (`!`) nos dois valores fornecidos. Aqui está um exemplo de código para o mesmo:

```js
const xor = (a, b) => (a || b) && !(a && b);
```

Aqui estão os valores de saída:

```js
xor(true, true); // false
xor(true, false); // true
xor(false, true); // true
xor(false, false); // false
```
