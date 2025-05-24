# Como Congelar Profundamente um Objeto em JavaScript

Para congelar profundamente um objeto em JavaScript, siga estes passos:

1.  Use `Object.keys()` para obter todas as propriedades do objeto passado.
2.  Itere sobre as propriedades usando `Array.prototype.forEach()`.
3.  Chame `Object.freeze()` recursivamente em todas as propriedades que são objetos, aplicando `deepFreeze()` conforme necessário.
4.  Finalmente, use `Object.freeze()` para congelar o objeto dado.

Aqui está o código:

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

Você pode testar o objeto congelado profundamente usando o seguinte código:

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // not allowed
val[1][0] = 4; // not allowed as well
```

O código acima lançará um erro porque o objeto `val` está profundamente congelado e não pode ser modificado.
