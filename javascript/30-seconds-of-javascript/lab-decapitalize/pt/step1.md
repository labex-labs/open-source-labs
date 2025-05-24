# Função JavaScript para Decapitalizar Strings

Para decapitalizar a primeira letra de uma string, use a seguinte função JavaScript:

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

Para usar esta função, abra o Terminal/SSH e digite `node`. Em seguida, chame a função `decapitalize`, passando a string que você deseja decapitalizar como o primeiro argumento.

Opcionalmente, você pode definir o segundo argumento `upperRest` como `true` para converter o restante da string para letras maiúsculas. Se `upperRest` não for fornecido, ele assume o valor padrão de `false`.

Aqui estão alguns exemplos:

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
