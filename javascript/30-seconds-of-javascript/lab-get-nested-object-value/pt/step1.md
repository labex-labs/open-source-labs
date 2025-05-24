# Como Recuperar Propriedades de Objetos Aninhados a partir de Strings de Caminho

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

A função a seguir recupera um conjunto de propriedades de um objeto usando seletores especificados em uma string de caminho. Para conseguir isso, siga estes passos:

1.  Use `Array.prototype.map()` para iterar por cada seletor e aplique `String.prototype.replace()` para substituir colchetes por pontos.
2.  Use `String.prototype.split()` para dividir cada seletor em um array de strings.
3.  Use `Array.prototype.filter()` para remover quaisquer valores vazios.
4.  Use `Array.prototype.reduce()` para recuperar o valor indicado por cada seletor.

Aqui está a função:

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

Você pode usar esta função para recuperar valores de um objeto aninhado usando uma string de caminho. Aqui está um exemplo:

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }]
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
