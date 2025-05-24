# Instruções do Gerador Cíclico

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`. Em seguida, crie um gerador que itera sobre o array fornecido indefinidamente. Aqui estão os passos:

1.  Use um loop `while` não terminante que irá `yield` um valor cada vez que `Generator.prototype.next()` for chamado.
2.  Use o operador módulo (`%`) com `Array.prototype.length` para obter o índice do próximo valor e incremente o contador após cada instrução `yield`.

Aqui está um exemplo da função `cycleGenerator`:

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

Você pode então usar a função da seguinte forma:

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

Com estas instruções, você pode criar um gerador cíclico que itera sobre qualquer array indefinidamente.
