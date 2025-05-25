# Função para Converter String em Título (Title Case)

Para converter uma string dada em título (title case), use a seguinte função. Ela usa `String.prototype.match()` para quebrar a string em palavras usando uma expressão regular apropriada. Em seguida, combina-as usando `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` e `String.prototype.toUpperCase()`. Isso capitaliza a primeira letra de cada palavra e adiciona um espaço em branco entre elas.

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

Aqui estão alguns exemplos de como usar a função:

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
