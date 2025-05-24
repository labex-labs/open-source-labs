# Criando um Objeto Set Congelado em JavaScript

Para criar um objeto `Set` congelado em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o construtor `Set` para criar um novo objeto `Set` a partir de um `iterable` (iterável).
3.  Defina os métodos `add`, `delete` e `clear` do objeto recém-criado como `undefined` para efetivamente congelar o objeto.

Aqui está um trecho de código de exemplo:

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// Output: Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

Este código cria um objeto `Set` congelado a partir de um iterável de números e retorna o objeto com seus métodos `add`, `delete` e `clear` definidos como `undefined`.
