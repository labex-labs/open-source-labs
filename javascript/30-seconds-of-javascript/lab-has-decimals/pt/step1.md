# Como Verificar se um Número Possui Dígitos Decimais

Para verificar se um número possui dígitos decimais, você pode usar o operador módulo em JavaScript. Siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador módulo (`%`) para verificar se o número é divisível por `1`.
3.  Se o resultado não for igual a zero, então o número possui dígitos decimais.

Aqui está um exemplo de código para verificar se um número possui dígitos decimais:

```js
const hasDecimals = (num) => num % 1 !== 0;
```

Você pode testar a função chamando-a com números diferentes, assim:

```js
hasDecimals(1); // false
hasDecimals(1.001); // true
```
