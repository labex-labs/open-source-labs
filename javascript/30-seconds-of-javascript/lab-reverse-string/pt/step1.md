# Aqui está uma função para inverter uma string:

Para inverter uma string, use o operador spread (`...`) e `Array.prototype.reverse()`. Combine os caracteres para obter uma string usando `Array.prototype.join()`. Aqui está o código:

```js
const reverseString = (str) => [...str].reverse().join("");
```

Exemplo de uso:

```js
reverseString("foobar"); // 'raboof'
```
