# CSV para JSON

Para converter uma string de valores separados por vírgula (CSV) em um array 2D de objetos e usá-la para praticar a codificação, abra o Terminal/SSH e digite `node`. A primeira linha da string é usada como linha de título. Aqui estão os passos para converter CSV para JSON:

1.  Use `Array.prototype.indexOf()` para encontrar o primeiro caractere de nova linha (`\n`).
2.  Use `Array.prototype.slice()` para remover a primeira linha (linha de título) e `String.prototype.split()` para separá-la em valores, usando o `delimiter` fornecido.
3.  Use `String.prototype.split()` para criar uma string para cada linha.
4.  Use `String.prototype.split()` para separar os valores em cada linha, usando o `delimiter` fornecido.
5.  Use `Array.prototype.reduce()` para criar um objeto para os valores de cada linha, com as chaves analisadas da linha de título.
6.  Omita o segundo argumento, `delimiter`, para usar um delimitador padrão de `,`.

Aqui está o código:

```js
const CSVToJSON = (data, delimiter = ",") => {
  const titles = data.slice(0, data.indexOf("\n")).split(delimiter);
  return data
    .slice(data.indexOf("\n") + 1)
    .split("\n")
    .map((v) => {
      const values = v.split(delimiter);
      return titles.reduce(
        (obj, title, index) => ((obj[title] = values[index]), obj),
        {}
      );
    });
};
```

Para testar a função, use os seguintes exemplos:

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
