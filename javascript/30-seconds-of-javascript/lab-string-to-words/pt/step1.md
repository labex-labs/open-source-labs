# Função para Converter String em um Array de Palavras

Para converter uma string fornecida em um array de palavras, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `String.prototype.split()` com um `pattern` fornecido (o padrão é non-alpha como uma regexp) para converter em um array de strings.
3.  Use o método `Array.prototype.filter()` para remover quaisquer strings vazias.
4.  Omita o segundo argumento, `pattern`, para usar a regexp padrão.

Aqui está uma função que implementa esses passos:

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

Você pode usar a função `words()` com diferentes strings para convertê-las em arrays de palavras:

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
