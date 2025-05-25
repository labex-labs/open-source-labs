# Convertendo _Query String_ para Objeto

Para converter uma _query string_ ou URL em um objeto, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `String.prototype.split()` para extrair os parâmetros da `url` fornecida.
3.  Use o construtor `URLSearchParams` para criar um objeto e convertê-lo em um array de pares chave-valor usando o operador spread (`...`).
4.  Use `Array.prototype.reduce()` para converter o array de pares chave-valor em um objeto.

Aqui está o código para converter a _query string_:

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {}
  );
```

Exemplo de uso:

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
