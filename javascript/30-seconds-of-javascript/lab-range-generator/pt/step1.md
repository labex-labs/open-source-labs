# Gerador de Intervalo (Range Generator)

Para gerar um intervalo de valores usando um passo especificado, use a seguinte função `rangeGenerator`. Abra o Terminal/SSH e digite `node` para começar a codificar.

- Use um loop `while` e `yield` para retornar cada valor, começando de `start` e terminando em `end`.
- Se você quiser usar um passo padrão de `1`, omita o terceiro argumento.

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

Aqui está um exemplo de como usar a função `rangeGenerator`:

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// Logs 6, 7, 8, 9
```
