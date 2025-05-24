# Como Atribuir Valores Padrão para Propriedades de Objetos

Para atribuir valores padrão para todas as propriedades em um objeto que são `undefined`, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Object.assign()` para criar um novo objeto vazio e copiar o original para manter a ordem das chaves.
3.  Use `Array.prototype.reverse()` e o operador de propagação (`...`) para combinar os valores padrão da esquerda para a direita.
4.  Finalmente, use `obj` novamente para sobrescrever as propriedades que originalmente tinham um valor.

Aqui está um trecho de código de exemplo:

```js
const defaults = (obj, ...defs) =>
  Object.assign({}, obj, ...defs.reverse(), obj);

defaults({ a: 1 }, { b: 2 }, { b: 6 }, { a: 3 }); // { a: 1, b: 2 }
```

Este trecho de código retornará um objeto que possui valores padrão para todas as propriedades que estavam indefinidas no objeto original.
