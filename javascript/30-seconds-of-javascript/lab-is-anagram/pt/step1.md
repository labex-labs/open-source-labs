# Função JavaScript para Verificar se uma String é um Anagrama

Para verificar se uma string é um anagrama de outra string, use a seguinte função JavaScript. Ela não diferencia maiúsculas e minúsculas e ignora espaços, pontuação e caracteres especiais.

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

Para usar a função, abra o Terminal/SSH e digite `node`. Em seguida, chame a função com duas strings como argumentos:

```js
isAnagram("iceman", "cinema"); // true
```

A função usa `String.prototype.toLowerCase()` e `String.prototype.replace()` com uma expressão regular apropriada para remover caracteres desnecessários. Ela também usa `String.prototype.split()`, `Array.prototype.sort()` e `Array.prototype.join()` em ambas as strings para normalizá-las e verificar se suas formas normalizadas são iguais.
