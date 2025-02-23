# Encadenamiento de funciones asíncronas

Para encadenar funciones asíncronas, abre la Terminal/SSH y escribe `node`. Luego, recorre un array de funciones que contienen eventos asíncronos y llama a la función `next` cuando cada evento asíncrono haya finalizado.

A continuación, se muestra un fragmento de código que demuestra cómo encadenar funciones asíncronas:

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
    console.log("0 segundos");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 segundo");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 segundos");
  }
]);
```
