# Algoritmo para Compactar Objetos

Para remover profundamente todos os valores falsos de um objeto ou array, use o seguinte algoritmo:

1.  Use recursão para chamar a função `compactObject()` em cada objeto ou array aninhado.
2.  Inicialize os dados iteráveis usando `Array.isArray()`, `Array.prototype.filter()` e `Boolean()`. Isso é feito para evitar arrays esparsos.
3.  Use `Object.keys()` e `Array.prototype.reduce()` para iterar sobre cada chave com um valor inicial apropriado.
4.  Use `Boolean()` para determinar a veracidade (truthiness) do valor de cada chave e adicione-o ao acumulador se for verdadeiro (truthy).
5.  Use `typeof` para determinar se um determinado valor é um `object` e chame a função novamente para compactá-lo profundamente.

Aqui está o código para a função `compactObject()`:

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

Para usar esta função, passe um objeto ou array como argumento para `compactObject()`. A função retornará um novo objeto ou array com todos os valores falsos removidos.

Por exemplo:

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
