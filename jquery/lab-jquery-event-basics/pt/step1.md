# Configurando Respostas a Eventos em Elementos DOM

> `index.html` já foi fornecido na VM.

O jQuery torna simples a configuração de respostas orientadas a eventos em elementos da página. Esses eventos são frequentemente acionados pela interação do usuário final com a página, como quando o texto é inserido em um elemento de formulário ou o ponteiro do mouse é movido. Em alguns casos, como os eventos de carregamento e descarregamento da página, o próprio navegador acionará o evento.

O jQuery oferece métodos convenientes para a maioria dos eventos nativos do navegador. Esses métodos — incluindo `.click()`, `.focus()`, `.blur()`, `.change()`, etc. — são abreviações do método `.on()` do jQuery. O método `on` é útil para vincular a mesma função de manipulador a vários eventos, quando você deseja fornecer dados ao manipulador de eventos, quando está trabalhando com eventos personalizados ou quando deseja passar um objeto de vários eventos e manipuladores.

```js
// Configuração de evento usando um método conveniente
$("p").click(function () {
  console.log("You clicked a paragraph!");
});
```

```js
// Configuração de evento equivalente usando o método `.on()`
$("p").on("click", function () {
  console.log("click");
});
```

> Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
