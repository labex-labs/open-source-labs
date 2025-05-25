# Função para Normalizar Quebras de Linha

Para normalizar as quebras de linha em uma string, você pode usar a seguinte função.

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- Use `String.prototype.replace()` com uma expressão regular para corresponder e substituir as quebras de linha pela versão `normalized`.
- Por padrão, a versão `normalized` é definida como `'\r\n'`.
- Para usar uma versão `normalized` diferente, passe-a como o segundo argumento.

Aqui estão alguns exemplos:

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
