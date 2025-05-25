# Instruções para Quebra de Linha (Word Wrap) em Strings

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

Este código quebra uma string em um número especificado de caracteres usando um caractere de quebra de linha. Para usá-lo, siga estas etapas:

1.  Use `String.prototype.replace()` e uma expressão regular para inserir um caractere de quebra especificado no espaço em branco mais próximo de `max` caracteres.
2.  Se você não quiser usar o valor padrão de `'\n'` para o terceiro argumento, `br`, você pode omiti-lo e fornecer seu próprio caractere.

Aqui está o código:

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

E aqui estão alguns exemplos de como usá-lo:

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
