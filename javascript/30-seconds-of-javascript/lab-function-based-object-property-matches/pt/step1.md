# Correspondência de Propriedades de Objetos com uma Função

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Esta função compara dois objetos e verifica se o primeiro objeto contém valores de propriedade equivalentes ao segundo. Ele faz isso com base em uma função fornecida.

Para usar esta função, siga estes passos:

- Use `Object.keys()` para recuperar todas as chaves do segundo objeto.
- Use `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` e a função fornecida para determinar se todas as chaves existem no primeiro objeto e têm valores equivalentes.
- Se nenhuma função for fornecida, os valores serão comparados usando o operador de igualdade.

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key]
  );
```

Aqui está um exemplo de como usar esta função:

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV)
); // true
```

Este exemplo verifica se os dois objetos têm valores equivalentes para a propriedade `greeting`. Ele usa a função `isGreeting` para garantir que ambos os valores sejam saudações válidas.
