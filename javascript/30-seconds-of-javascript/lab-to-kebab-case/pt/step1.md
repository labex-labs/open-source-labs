# Convertendo uma string para kebab case

Para converter uma string para kebab case, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `String.prototype.match()` para quebrar a string em palavras usando uma expressão regular apropriada.
3.  Use `Array.prototype.map()`, `Array.prototype.join()` e `String.prototype.toLowerCase()` para combinar as palavras, adicionando `-` como separador.

Aqui está um exemplo de função que realiza a conversão:

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

Você pode usar esta função para converter strings para kebab case, como mostrado abaixo:

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); // 'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
