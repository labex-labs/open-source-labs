# Criando uma _Promise_ com um Atraso

Para criar uma nova _promise_ que resolve após um período de tempo específico, siga estes passos:

1.  Use o construtor `Promise` para criar uma nova _promise_.
2.  Dentro da função _executor_ (executora) da _promise_, use `setTimeout()` para chamar a função `resolve` da _promise_ com o `value` (valor) fornecido após o `delay` (atraso) especificado.

Aqui está um exemplo de implementação de `resolveAfter()`:

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

Agora você pode chamar `resolveAfter()` para obter uma _promise_ que resolve para o valor fornecido após o atraso especificado:

```js
resolveAfter("Hello", 1000);
// Retorna uma promise que resolve para 'Hello' após 1s
```

Para começar a praticar a codificação, abra o Terminal ou SSH e digite `node`.
