# Como Serializar um Cookie

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`. Em seguida, siga estes passos para serializar um par nome-valor de cookie em uma string de cabeçalho Set-Cookie:

1.  Use literais de template e `encodeURIComponent()` para criar a string apropriada.
2.  Implemente a função `serializeCookie` passando os parâmetros `name` e `val`.
3.  A função retornará uma string que é devidamente serializada.

Aqui está um exemplo de como usar a função `serializeCookie`:

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

Neste exemplo, a função `serializeCookie` recebe `foo` como o nome do cookie e `bar` como o valor do cookie, e retorna uma string de cookie serializada de `foo=bar`.
