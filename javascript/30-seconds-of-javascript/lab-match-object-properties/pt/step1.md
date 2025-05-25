# Como Comparar Propriedades de Objetos em JavaScript

Para comparar dois objetos e verificar se eles possuem os mesmos valores de propriedade, use a função `matches`. Veja como usá-la:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.
2.  Copie e cole o código da função `matches` em seu arquivo JavaScript.
3.  Chame a função e passe dois objetos como argumentos. O primeiro objeto é aquele que você deseja comparar, e o segundo objeto é aquele com o qual você deseja compará-lo.

```js
matches({ age: 25, hair: "long", beard: true }, { hair: "long", beard: true });
// true
matches({ hair: "long", beard: true }, { age: 25, hair: "long", beard: true });
// false
```

A função `matches` usa `Object.keys()` para obter todas as chaves do segundo objeto e, em seguida, verifica se todas as chaves existem no primeiro objeto e possuem os mesmos valores usando `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` e comparação estrita.
