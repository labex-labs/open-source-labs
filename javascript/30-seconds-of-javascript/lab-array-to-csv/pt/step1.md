# Converter Array 2D para CSV

Para converter um array 2D em uma string de valores separados por vírgula (CSV), siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.map()` e `Array.prototype.join()` para combinar arrays 1D individuais (linhas) em strings, usando o `delimiter` fornecido.
3.  Use `Array.prototype.join()` para combinar todas as linhas em uma string CSV, separando cada linha com uma quebra de linha (`\n`).
4.  Se você quiser usar o delimitador padrão de `,`, omita o segundo argumento, `delimiter`.

Aqui está um exemplo do código:

```js
const arrayToCSV = (arr, delimiter = ",") =>
  arr
    .map((v) =>
      v
        .map((x) => (isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x))
        .join(delimiter)
    )
    .join("\n");
```

Você pode testar a função executando as seguintes linhas de código:

```js
arrayToCSV([
  ["a", "b"],
  ["c", "d"]
]); // '"a","b"\n"c","d"'
arrayToCSV(
  [
    ["a", "b"],
    ["c", "d"]
  ],
  ";"
); // '"a";"b"\n"c";"d"'
arrayToCSV([
  ["a", '"b" great'],
  ["c", 3.1415]
]);
// '"a","""b"" great"\n"c",3.1415'
```
