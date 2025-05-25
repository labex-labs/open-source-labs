# Verificar se os Argumentos do Processo Contêm Flags

Para verificar se os argumentos do processo atual contêm flags especificadas, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.every()` e `Array.prototype.includes()` para verificar se `process.argv` contém todas as flags especificadas.
3.  Use uma expressão regular para testar se as flags especificadas são prefixadas com `-` ou `--` e prefixe-as de acordo.

Aqui está um trecho de código que mostra como implementar isso:

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag)
  );
```

Você pode testar a função com diferentes flags assim:

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
