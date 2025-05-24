# Verificador de Propriedades (Property Checker)

Para verificar se uma propriedade específica de um objeto atende a uma determinada condição, use a função `checkProp`. Esta função cria uma função curried que recebe uma função predicado (predicate function) e um nome de propriedade como argumentos. A função retornada então recebe um objeto e retorna `true` ou `false` com base em se a propriedade especificada atende à condição especificada pela função predicado.

Aqui está uma implementação de exemplo de `checkProp`:

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

E aqui estão alguns exemplos de como você pode usá-la:

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set uses Size, not length)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

Em resumo, a função `checkProp` permite que você verifique facilmente o valor de uma propriedade específica em um objeto, especificando uma função predicado para essa propriedade.
