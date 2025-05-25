# Função JavaScript para Analisar Cookies HTTP

Para analisar (parse) uma string de cabeçalho Cookie HTTP em JavaScript e retornar um objeto com todos os pares nome-valor dos cookies, siga estes passos:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `String.prototype.split()` para separar os pares chave-valor uns dos outros.
- Use `Array.prototype.map()` e `String.prototype.split()` para separar as chaves dos valores em cada par.
- Use `Array.prototype.reduce()` e `decodeURIComponent()` para criar um objeto com todos os pares chave-valor.

Aqui está um exemplo da função `parseCookie()` que implementa os passos acima:

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

Você pode testar a função da seguinte forma:

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
