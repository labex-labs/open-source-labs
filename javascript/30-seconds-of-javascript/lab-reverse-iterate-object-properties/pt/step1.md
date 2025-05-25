# Como iterar sobre as próprias propriedades de um objeto em ordem inversa

Para iterar sobre as próprias propriedades de um objeto em ordem inversa e executar um _callback_ para cada uma, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Object.keys()` para obter todas as propriedades do objeto.
3.  Use `Array.prototype.reverse()` para inverter a ordem das propriedades.
4.  Use `Array.prototype.forEach()` para executar a função fornecida para cada par chave-valor.
5.  A função _callback_ deve ter três argumentos: o valor, a chave e o objeto.

Aqui está o código:

```js
const forOwnRight = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .forEach((key) => fn(obj[key], key, obj));
```

Você pode usar esta função com qualquer objeto e função _callback_. Por exemplo, para registrar os valores de `{ foo: 'bar', a: 1 }` em ordem inversa, você pode usar o seguinte código:

```js
forOwnRight({ foo: "bar", a: 1 }, (v) => console.log(v)); // 1, 'bar'
```
