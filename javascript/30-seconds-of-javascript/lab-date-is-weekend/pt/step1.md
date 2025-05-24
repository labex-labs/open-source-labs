# Verificando se a Data é um Fim de Semana

Para verificar se uma determinada data é um fim de semana, siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use o método `Date.prototype.getDay()` para obter o dia da semana como um número (0-6), sendo domingo 0 e sábado 6.
- Verifique se o dia é um fim de semana usando o operador módulo (`%`) e comparando-o a 0 ou 6.
- Omita o argumento, `d`, para usar a data atual como padrão.

Aqui está um trecho de código de exemplo que você pode usar:

```js
const isWeekend = (d = new Date()) => d.getDay() % 6 === 0;
```

Para testar a função, simplesmente chame-a sem nenhum argumento:

```js
isWeekend(); // true or false (depending on the current date)
```

Isso retornará `true` se a data atual for um fim de semana (sábado ou domingo) e `false` caso contrário.
