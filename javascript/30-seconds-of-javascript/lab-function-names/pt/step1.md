# Como Obter os Nomes das Propriedades de Função de um Objeto em JavaScript

Para obter um array com os nomes das propriedades de função de um objeto, use a função `functions` fornecida abaixo. Esta função também pode, opcionalmente, incluir propriedades herdadas.

Veja como usar a função `functions`:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Object.keys()` para iterar sobre as próprias propriedades do objeto.
3. Se você quiser incluir propriedades herdadas, defina o argumento `inherited` como `true` e use `Object.getPrototypeOf()` para obter as propriedades herdadas do objeto.
4. Use `Array.prototype.filter()` para manter apenas as propriedades que são funções.
5. Omita o segundo argumento, `inherited`, para não incluir propriedades herdadas por padrão.

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

Aqui está um exemplo de uso da função `functions`:

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
