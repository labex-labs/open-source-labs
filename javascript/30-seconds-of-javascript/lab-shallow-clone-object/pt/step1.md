# Como Criar um Clone Raso de um Objeto

Para criar um _shallow clone_ (clone raso) de um objeto, use `Object.assign()` e um objeto vazio (`{}`). Siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o seguinte código para criar um clone raso do objeto original:

```js
const shallowClone = (obj) => Object.assign({}, obj);
```

3.  Para clonar o objeto, use a função `shallowClone()` da seguinte forma:

```js
const a = { x: true, y: 1 };
const b = shallowClone(a); // a !== b
```

Neste exemplo, `a` e `b` são dois objetos diferentes, mas possuem os mesmos valores.
