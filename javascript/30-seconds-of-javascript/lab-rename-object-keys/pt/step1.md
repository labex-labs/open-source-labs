# Como Renomear Chaves de Objetos em JavaScript

Para renomear múltiplas chaves de objetos com os valores fornecidos, você pode usar a função `renameKeys`. Aqui estão os passos que você precisa seguir:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Object.keys()` em combinação com `Array.prototype.reduce()` e o operador spread (`...`) para obter as chaves do objeto e renomeá-las de acordo com `keysMap`.
3.  Passe o `keysMap` e o objeto (`obj`) como argumentos para a função `renameKeys`.
4.  A função `renameKeys` retorna um novo objeto com as chaves renomeadas.

Aqui está um exemplo de como usar a função `renameKeys`:

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
