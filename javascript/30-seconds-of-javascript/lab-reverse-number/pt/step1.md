# Invertendo um Número

Para inverter um número usando JavaScript, você pode usar a função `reverseNumber()` com as seguintes etapas:

1.  Converta o número `n` em uma string usando `Object.prototype.toString()`.
2.  Use `String.prototype.split()`, `Array.prototype.reverse()` e `Array.prototype.join()` para obter o valor invertido de `n` como uma string.
3.  Converta a string de volta para um número usando `parseFloat()`.
4.  Preserve o sinal do número usando `Math.sign()`.

Aqui está o código para a função `reverseNumber()`:

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

Você pode testar a função com estes exemplos:

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
