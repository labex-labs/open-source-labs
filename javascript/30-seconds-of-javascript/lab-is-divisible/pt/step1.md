# Verificar se um Número é Divisível

Para verificar se um número é divisível por outro número em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador módulo (`%`) para verificar se o resto da divisão é igual a `0`. Se for, então o número é divisível.

Aqui está um exemplo de função que verifica se o primeiro argumento numérico é divisível pelo segundo:

```js
const isDivisible = (dividend, divisor) => dividend % divisor === 0;
```

Você pode testar esta função com `isDivisible(6, 3)`, que deve retornar `true` já que 6 é divisível por 3.
