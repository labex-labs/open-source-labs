# Convertendo JSON para CSV

Para converter um array de objetos em uma string de valores separados por vírgula (CSV) com colunas especificadas, use a seguinte função:

```js
const JSONtoCSV = (arr, columns, delimiter = ",") =>
  [
    columns.join(delimiter),
    ...arr.map((obj) =>
      columns.reduce(
        (acc, key) =>
          `${acc}${!acc.length ? "" : delimiter}"${!obj[key] ? "" : obj[key]}"`,
        ""
      )
    )
  ].join("\n");
```

Para usá-la, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Chame a função `JSONtoCSV` com os seguintes argumentos:
    - `arr`: um array de objetos a serem convertidos.
    - `columns`: um array de strings que especificam as colunas a serem incluídas na saída CSV.
    - `delimiter`: uma string opcional que especifica o delimitador a ser usado (o valor padrão é `','`).
3.  A função retornará uma string CSV que contém apenas as colunas especificadas e os valores dos objetos.
4.  Se nenhum delimitador for especificado, o delimitador padrão `','` será usado.
5.  Exemplos de como usar a função são fornecidos no bloco de código abaixo.

```js
JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"]
); // 'a,b\n"1","2"\n"3","4"\n"6",""\n"","7"'

JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"],
  ";"
); // 'a;b\n"1";"2"\n"3";"4"\n"6";""\n"";"7"'
```
