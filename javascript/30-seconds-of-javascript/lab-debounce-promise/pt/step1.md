# Debounce Promise (Promise com Debounce)

Para criar uma função _debounced_ (com debounce) que retorna uma _promise_, atrasando a invocação da função fornecida até que pelo menos `ms` milissegundos tenham decorrido desde a última vez que foi invocada, use as seguintes etapas:

1.  Toda vez que a função _debounced_ é invocada, limpe o _timeout_ pendente atual com `clearTimeout()`, então use `setTimeout()` para criar um novo _timeout_ que atrasa a invocação da função até que pelo menos `ms` milissegundos tenham decorrido.
2.  Use `Function.prototype.apply()` para aplicar o contexto `this` à função e fornecer os argumentos necessários.
3.  Crie uma nova `Promise` e adicione seus _callbacks_ `resolve` e `reject` à pilha de _promises_ `pending`.
4.  Quando `setTimeout()` é chamado, copie a pilha atual (pois ela pode mudar entre a chamada da função fornecida e sua resolução), limpe-a e chame a função fornecida.
5.  Quando a função fornecida resolve/rejeita, resolva/rejeite todas as _promises_ na pilha (copiada quando a função foi chamada) com os dados retornados.
6.  Omita o segundo argumento, `ms`, para definir o _timeout_ em um padrão de `0` ms.

Aqui está o código para a função `debouncePromise()`:

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

Aqui está um exemplo de como usar `debouncePromise()`:

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// Will log ['resolved', 'bar'] both times
```
