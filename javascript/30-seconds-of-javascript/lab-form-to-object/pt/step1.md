# Convertendo um Formulário em um Objeto

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Você pode codificar um conjunto de elementos de formulário como um objeto usando as seguintes etapas:

1.  Use o construtor `FormData` para converter o `form` HTML em `FormData`.
2.  Converta o `FormData` em um array usando `Array.from()`.
3.  Colete o objeto do array usando `Array.prototype.reduce()`.

Aqui está um trecho de código de exemplo:

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

Para converter um formulário específico, você pode chamar a função `formToObject` e passar o elemento do formulário como um argumento:

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
