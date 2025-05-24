# Função de Formatação de Números

Para formatar um número usando a ordem de formatação de números local, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Number.prototype.toLocaleString()` para converter um número usando os separadores de formatação de números local.
3.  Passe o número que você deseja formatar como um argumento para a função.

Aqui está um exemplo de implementação:

```js
const formatNumber = (num) => num.toLocaleString();
```

E aqui estão alguns exemplos de como usar a função:

```js
formatNumber(123456); // '123,456' em `en-US`
formatNumber(15675436903); // '15.675.436.903' em `de-DE`
```
