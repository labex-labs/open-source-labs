# Encadeando Funções Assíncronas

Para encadear funções assíncronas, abra o Terminal/SSH e digite `node`. Em seguida, itere sobre um array de funções contendo eventos assíncronos e chame a função `next` quando cada evento assíncrono for concluído.

Aqui está um trecho de código que demonstra como encadear funções assíncronas:

```js
const chainAsync = (fns) => {
  let curr = 0;
  const last = fns[fns.length - 1];
  const next = () => {
    const fn = fns[curr++];
    fn === last ? fn() : fn(next);
  };
  next();
};

chainAsync([
  (next) => {
    console.log("0 seconds");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 second");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 second");
  }
]);
```
