# Prática de Código com Gerador de Repetição

Para praticar a codificação, abra o Terminal/SSH e digite `node` para criar um gerador que repete o valor fornecido indefinidamente. Use um loop `while` não terminante que irá `yield` um valor toda vez que `Generator.prototype.next()` for chamado. Em seguida, use o valor de retorno da instrução `yield` para atualizar o valor retornado se o valor passado não for `undefined`.

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

Para testar o gerador, crie uma instância dele usando o valor `5` e chame `repeater.next()` para obter o próximo valor na sequência. A saída será `{ value: 5, done: false }`. Chamar `repeater.next()` novamente retornará o mesmo valor. Para alterar o valor, chame `repeater.next(4)`, que retornará `{ value: 4, done: false }`. Finalmente, chamar `repeater.next()` retornará o valor atualizado, `{ value: 4, done: false }`.
