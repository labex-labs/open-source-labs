# Objeto com Parâmetros de URL

Para criar um objeto que contenha os parâmetros da URL atual, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `String.prototype.match()` com uma expressão regular apropriada para extrair todos os pares chave-valor.
3. Use `Array.prototype.reduce()` para mapear e combiná-los em um único objeto.
4. Passe `location.search` como argumento para aplicar à URL atual.

Aqui está o código:

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)),
      a
    ),
    {}
  );
```

Você pode usar esta função com qualquer URL para obter um objeto com seus parâmetros. Aqui estão alguns exemplos:

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam', surname: 'Smith'}
```
