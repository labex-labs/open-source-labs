# Estendendo Eventos a Novos Elementos da Página

É importante notar que `.on()` só pode criar ouvintes de eventos em elementos que existem no momento em que você configura os ouvintes. Por exemplo:

```js
$(document).ready(function () {
  // Now create a new button element with the alert class.
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // Sets up click behavior on all button elements with the alert class
  // that exist in the DOM when the instruction was executed
  $("button.alert").on("click", function () {
    console.log("A button with the alert class was clicked!");
  });
});
```

Se elementos semelhantes forem criados após a configuração dos ouvintes de eventos, eles não herdarão automaticamente os comportamentos de evento que você configurou anteriormente.

> Você pode atualizar a aba **Web 8080** para visualizar a página web.
