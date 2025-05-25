# Configurando Múltiplas Respostas a Eventos

Com bastante frequência, os elementos em sua aplicação serão vinculados a múltiplos eventos. Se múltiplos eventos devem compartilhar a mesma função de tratamento (handler), você pode fornecer os tipos de evento como uma lista separada por espaços para `.on()`:

```js
// Múltiplos eventos, mesmo manipulador (handler)
$("div").on(
  "click change", // Vincular manipuladores (handlers) para múltiplos eventos
  function () {
    console.log("An input was clicked or changed!");
  }
);
```

Quando cada evento tem seu próprio manipulador (handler), você pode passar um objeto para `.on()` com um ou mais pares chave/valor, sendo a chave o nome do evento e o valor a função para tratar o evento.

```js
// Vinculando múltiplos eventos com diferentes manipuladores (handlers)
$("div").on({
  click: function () {
    console.log("clicked!");
  },
  mouseover: function () {
    console.log("hovered!");
  }
});
```

> Você pode atualizar a aba **Web 8080** para visualizar a página web.
