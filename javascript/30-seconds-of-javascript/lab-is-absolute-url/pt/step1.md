# Função para Verificar se uma String é uma URL Absoluta

Para verificar se uma determinada string é uma URL absoluta, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `RegExp.prototype.test()` para testar se a string é uma URL absoluta.
3.  A função deve ser definida como `const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);`
4.  A função recebe um argumento de string `str` e retorna `true` se a string for uma URL absoluta, e `false` caso contrário.
5.  Teste a função usando os exemplos fornecidos:

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
