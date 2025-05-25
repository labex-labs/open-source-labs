# Como Converter um Número para Formato com Marca Decimal

Para converter um número para o formato com marca decimal, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Number.prototype.toLocaleString()` para converter o número para o formato com marca decimal.
3.  O seguinte código pode ser usado para este processo:

```js
const toDecimalMark = (num) => num.toLocaleString("en-US");
```

Aqui está um exemplo de como usar esta função:

```js
toDecimalMark(12305030388.9087); // '12,305,030,388.909'
```

Isso converterá o número `12305030388.9087` para a string formatada com marca decimal `'12,305,030,388.909'`.
