# Junção e Normalização de Segmentos de URL

Para juntar os segmentos de URL fornecidos e normalizar a URL resultante, siga os passos abaixo:

1.  Use `Array.prototype.join()` para combinar os segmentos de URL.
2.  Use uma série de chamadas `String.prototype.replace()` com várias expressões regulares para normalizar a URL resultante, fazendo o seguinte:
    - Removendo barras duplas
    - Adicionando barras adequadas para o protocolo
    - Removendo barras antes dos parâmetros
    - Combinando parâmetros com `'&'` e normalizando o delimitador do primeiro parâmetro.

Use o trecho de código abaixo para juntar e normalizar segmentos de URL:

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

Exemplo de uso:

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
