# Recuperando a URL Base

Para recuperar a URL base de uma determinada URL, siga estes passos:

1. Abra o Terminal/SSH.
2. Digite `node` para começar a praticar a codificação.
3. Use a seguinte função JavaScript para obter a URL atual sem quaisquer parâmetros ou identificadores de fragmento:

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. Substitua `url` pela URL da qual você deseja recuperar a URL base.
5. A função removerá tudo após `'?'` ou `'#'`, se encontrado, e retornará a URL base.
6. Aqui está um exemplo:

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
