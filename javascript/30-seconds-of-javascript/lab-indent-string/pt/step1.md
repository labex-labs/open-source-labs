# Uma Função para Indentar Strings em JavaScript

Para adicionar indentação a cada linha numa string fornecida, pode usar a função `indentString()` em JavaScript. Esta função recebe três argumentos: `str`, `count` e `indent`.

- O argumento `str` representa a string que deseja indentar.
- O argumento `count` determina quantas vezes deseja indentar cada linha.
- O argumento `indent` é opcional e representa o caractere que deseja usar para a indentação. Se não o fornecer, o valor padrão é um único caractere de espaço (`' '`).

Aqui está o código para a função `indentString()`:

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

Para usar esta função, basta chamá-la com os argumentos desejados. Aqui estão alguns exemplos:

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

No primeiro exemplo, `indentString('Lorem\nIpsum', 2)` retorna `'  Lorem\n  Ipsum'`, o que significa que cada linha da string de entrada foi indentada duas vezes com caracteres de espaço.

No segundo exemplo, `indentString('Lorem\nIpsum', 2, '_')` retorna `'__Lorem\n__Ipsum'`, o que significa que cada linha da string de entrada foi indentada duas vezes com caracteres de sublinhado (`'_'`).
