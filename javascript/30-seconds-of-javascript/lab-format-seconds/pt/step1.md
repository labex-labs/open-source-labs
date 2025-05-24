# Função para Formatar Segundos como Tempo ISO

Para usar este código, abra o Terminal/SSH e digite `node`. Esta função recebe um número de segundos como argumento e retorna o formato de tempo ISO. Veja como funciona:

- Divida o número de segundos pelos valores apropriados para obter os valores correspondentes para `hora` (hour), `minuto` (minute) e `segundo` (second).
- Armazene o sinal do número em uma variável para adicioná-lo ao resultado.
- Use `Array.prototype.map()` em combinação com `Math.floor()` e `String.prototype.padStart()` para transformar em string e formatar cada segmento.
- Use `Array.prototype.join()` para combinar os valores em uma string.

Aqui está o código:

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

Você pode testar a função com estes exemplos:

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
