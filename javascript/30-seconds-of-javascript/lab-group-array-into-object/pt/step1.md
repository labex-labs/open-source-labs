# Como Agrupar um Array em um Objeto

Para agrupar um array em um objeto, siga estes passos:

1.  Abra o Terminal ou SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.reduce()` para construir um objeto a partir dos dois arrays.
3.  Forneça um array de identificadores de propriedade válidos e um array de valores.
4.  Se o comprimento do array de propriedades for maior que o array de valores, as chaves restantes serão definidas como `undefined`.
5.  Se o comprimento do array de valores for maior que o array de propriedades, os valores restantes serão ignorados.

Aqui está um trecho de código de exemplo que demonstra como agrupar um array em um objeto:

```js
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

zipObject(["a", "b", "c"], [1, 2]); // {a: 1, b: 2, c: undefined}
zipObject(["a", "b"], [1, 2, 3]); // {a: 1, b: 2}
```
