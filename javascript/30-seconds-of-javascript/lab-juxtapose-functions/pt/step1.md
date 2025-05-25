# Explicação das Funções Juxtapostas (Juxtapose Functions)

Para usar a função `juxt`, primeiro abra o Terminal/SSH e digite `node` para começar a praticar a codificação. A função `juxt` recebe várias funções como argumentos e retorna uma função que é a justaposição dessas funções.

Para criar a função `juxt`, use `Array.prototype.map()` para retornar uma `fn` que pode receber um número variável de `args`. Quando `fn` é chamada, ela deve retornar um array contendo o resultado da aplicação de cada `fn` aos `args`.

Aqui está um exemplo de implementação da função `juxt`:

```js
const juxt =
  (...fns) =>
  (...args) =>
    [...fns].map((fn) => [...args].map(fn));
```

Depois de definir a função `juxt`, você pode usá-la passando qualquer número de funções como argumentos, seguido por qualquer número de argumentos para passar para essas funções.

Aqui estão alguns exemplos de como usar a função `juxt`:

```js
juxt(
  (x) => x + 1,
  (x) => x - 1,
  (x) => x * 10
)(1, 2, 3); // [[2, 3, 4], [0, 1, 2], [10, 20, 30]]
```

```js
juxt(
  (s) => s.length,
  (s) => s.split(" ").join("-")
)("happy coding"); // [[18], ['happy-coding']]
```

No primeiro exemplo, a função `juxt` recebe três funções como argumentos e retorna uma nova função. Quando essa nova função é chamada com os argumentos `1, 2, 3`, ela aplica cada uma das três funções a esses argumentos e retorna um array de arrays contendo os resultados.

No segundo exemplo, a função `juxt` recebe duas funções como argumentos e retorna uma nova função. Quando essa nova função é chamada com o argumento `'happy-coding'`, ela aplica cada uma das duas funções a esse argumento e retorna um array de arrays contendo os resultados.
