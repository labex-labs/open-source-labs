# Verificação de Luhn (Luhn Check)

Para usar o Algoritmo de Luhn para validação de números de identificação, como números de cartão de crédito, números IMEI, números de identificação de provedores nacionais (National Provider Identifier numbers), siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use os seguintes métodos: `String.prototype.split()`, `Array.prototype.reverse()`, `Array.prototype.map()` e `parseInt()` em combinação para obter um array de dígitos.
3.  Use `Array.prototype.shift()` para obter o último dígito.
4.  Use `Array.prototype.reduce()` para implementar o Algoritmo de Luhn.
5.  Retorne `true` se `sum` for divisível por `10`, `false` caso contrário.

Aqui está o código:

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

Você pode testar a função de Verificação de Luhn usando estes exemplos:

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
