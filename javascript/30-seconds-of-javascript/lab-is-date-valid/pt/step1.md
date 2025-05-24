# Como Verificar se uma Data é Válida

Para verificar se uma data é válida, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador spread (`...`) para passar o array de argumentos para o construtor `Date`.
3.  Use `Date.prototype.valueOf()` e `Number.isNaN()` para verificar se um objeto `Date` válido pode ser criado a partir dos valores fornecidos.

Aqui está um exemplo de trecho de código:

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

Você pode testar a função com diferentes valores, como mostrado abaixo:

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
