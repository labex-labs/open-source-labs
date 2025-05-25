# Complemento Lógico

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Para obter o complemento lógico de uma função `fn`, use a função `complement`. Esta função retorna outra função que aplica o operador lógico not (`!`) no resultado da chamada de `fn` com quaisquer argumentos fornecidos.

Aqui está um exemplo de trecho de código:

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

Para usar esta função, defina uma função predicado, por exemplo, `isEven`, que retorna `true` se um determinado número for par. Você pode então obter o complemento lógico desta função usando a função `complement`, conforme mostrado abaixo:

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
