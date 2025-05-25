# Algo Após a Conclusão de uma Animação

Um erro comum ao implementar efeitos jQuery é assumir que a execução do próximo método em sua cadeia aguardará até que a animação seja executada até a conclusão.

```js
$("div.hidden").fadeIn(1500).addClass("lookAtMe");
```

É importante perceber que `.fadeIn()` acima apenas inicia a animação. Uma vez iniciada, a animação é implementada alterando rapidamente as propriedades CSS em um loop `setInterval()` do JavaScript. Quando você chama `.fadeIn()`, ele inicia o loop de animação e, em seguida, retorna o objeto jQuery, passando-o para `.addClass()`, que então adicionará a classe de estilo `lookAtMe` enquanto o loop de animação está apenas começando.

Para adiar uma ação até que uma animação seja executada até a conclusão, você precisa usar uma função de callback de animação. Você pode especificar seu callback de animação como o segundo argumento passado para qualquer um dos métodos de animação discutidos acima. Para o trecho de código acima, podemos implementar um callback da seguinte forma:

```js
// Fade in todos os parágrafos ocultos; em seguida, adicione uma classe de estilo a eles (correto com o callback de animação)
$("div.hidden").fadeIn(1500, function () {
  // this = elemento DOM que acabou de terminar de ser animado
  $(this).addClass("lookAtMe");
});
```

Observe que você pode usar a palavra-chave `this` para se referir ao elemento DOM que está sendo animado. Observe também que o callback será chamado para cada elemento no objeto jQuery. Isso significa que, se seu seletor não retornar nenhum elemento, seu callback de animação nunca será executado! Você pode resolver esse problema testando se sua seleção retornou algum elemento; caso contrário, você pode simplesmente executar o callback imediatamente.

```js
// Execute um callback mesmo que não houvesse elementos para animar
var someElement = $("#nonexistent");

var cb = function () {
  console.log("done!");
};

if (someElement.length) {
  someElement.fadeIn(300, cb);
} else {
  cb();
}
```

> Você pode atualizar a aba **Web 8080** para visualizar a página web.
