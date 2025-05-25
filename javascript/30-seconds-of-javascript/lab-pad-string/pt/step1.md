# Função para Preencher String (Pad String)

Para preencher uma string em ambos os lados com o caractere especificado, se ela for menor que o `length` especificado, use a seguinte função:

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

A função usa `String.prototype.padStart()` e `String.prototype.padEnd()` para preencher ambos os lados da string fornecida. Você pode omitir o terceiro argumento, `char`, para usar o caractere de espaço em branco como o caractere de preenchimento padrão.

Aqui estão alguns exemplos de como usar a função `pad()`:

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
