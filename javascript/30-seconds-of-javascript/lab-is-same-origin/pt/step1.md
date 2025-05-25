# Verificar se Duas URLs Estão na Mesma Origem

Para verificar se duas URLs estão na mesma origem:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Use `URL.protocol` e `URL.host` para verificar se ambas as URLs têm o mesmo protocolo e host.

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. Crie dois objetos URL com as URLs que você deseja comparar.

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. Chame a função `isSameOrigin` com os dois objetos URL como argumentos para obter uma saída booleana.

```js
isSameOrigin(origin, destination); // true
```

5. Você também pode testar a função com outras URLs para ver se elas estão na mesma origem ou não.

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
