# Convertendo CSV para um Array

Para converter uma string de valores separados por vírgula (CSV) em um array 2D, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.
2.  Use `Array.prototype.indexOf()` para localizar o primeiro caractere de nova linha (`\n`).
3.  Use `Array.prototype.slice()` para remover a primeira linha (linha de título) se `omitFirstRow` estiver definido como `true`.
4.  Use `String.prototype.split()` para criar uma string para cada linha.
5.  Use `String.prototype.split()` para separar os valores em cada linha usando o `delimiter` fornecido.
6.  Se você não fornecer o segundo argumento, `delimiter`, o delimitador padrão de `','` será usado.
7.  Se você não fornecer o terceiro argumento, `omitFirstRow`, a primeira linha (linha de título) da string CSV será incluída.

Aqui está o código para converter CSV em um array:

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

Você pode usar os seguintes exemplos para testar a função:

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
