# Função para Combinar Arrays de Objetos com Base em uma Chave Especificada

Para combinar dois arrays de objetos com base em uma chave específica, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.reduce()` com um acumulador de objeto para combinar todos os objetos em ambos os arrays com base na `prop` fornecida.
3.  Use `Object.values()` para converter o objeto resultante em um array e retorná-lo.

Aqui está a função que você pode usar:

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {})
  );
```

Aqui está um exemplo de como usar esta função:

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" }
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
