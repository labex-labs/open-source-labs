# Instruções para Clonar Profundamente um Objeto

Para clonar profundamente um objeto, siga estes passos:

1.  Crie uma nova instância de terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use recursão para clonar primitivos, arrays e objetos, excluindo instâncias de classes.
3.  Verifique se o objeto passado é `null` e, se for, retorne `null`.
4.  Use `Object.assign()` e um objeto vazio (`{}`) para criar uma cópia rasa (shallow clone) do original.
5.  Use `Object.keys()` e `Array.prototype.forEach()` para determinar quais pares chave-valor precisam ser clonados profundamente.
6.  Se o objeto for um `Array`, defina o `length` do `clone` para o do original e use `Array.from()` para criar um clone.
7.  Use o seguinte código para implementar a clonagem profunda:

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

Use o seguinte código para testar sua função de clonagem profunda:

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a !== b, a.obj !== b.obj
```
