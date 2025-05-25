# Função para Converter String em URL Slug

Para converter uma string em um slug que pode ser usado em uma URL, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use os métodos `String.prototype.toLowerCase()` e `String.prototype.trim()` para normalizar a string.
3. Use o método `String.prototype.replace()` para substituir espaços, traços e sublinhados por `-`, e remover caracteres especiais.
4. Implemente o seguinte código:

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. Teste a função com a entrada `slugify('Hello World!');` e ela deve retornar a saída `'hello-world'`.
