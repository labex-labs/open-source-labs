# Função JavaScript para Capitalizar a Primeira Letra de uma String

Para capitalizar a primeira letra de uma string em JavaScript, use a seguinte função:

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

Esta função utiliza destruturação de array e `String.prototype.toUpperCase()` para capitalizar a primeira letra da string. O argumento `lowerRest` é opcional e pode ser definido como `true` para converter o restante da string para minúsculas.

Aqui está um exemplo de como usar esta função:

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
