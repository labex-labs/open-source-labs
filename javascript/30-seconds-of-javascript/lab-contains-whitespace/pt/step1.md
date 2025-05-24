# Verificando Espaços em Branco em uma String

Para verificar se uma string contém caracteres de espaço em branco, siga os passos abaixo:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `RegExp.prototype.test()` com uma expressão regular apropriada para verificar se a string fornecida contém quaisquer caracteres de espaço em branco.
- Aqui está um trecho de código de exemplo:

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- Para testar a função, chame `containsWhitespace` com uma string como argumento. Ela retornará `true` se a string contiver caracteres de espaço em branco, caso contrário, retornará `false`.

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
