# Eventos

> `index.html` já foi fornecido na VM.

A real interatividade em um site requer manipuladores de eventos. Estas são estruturas de código que escutam por atividade no navegador e executam código em resposta. O exemplo mais óbvio é o tratamento do [evento de clique](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event), que é disparado pelo navegador quando você clica em algo com o mouse. Para demonstrar isso, insira o seguinte no seu console e, em seguida, clique na página web atual:

```js
document.querySelector("html").addEventListener("click", function () {
  alert("Ai! Pare de me cutucar!");
});
```

Há várias maneiras de anexar um manipulador de eventos a um elemento.
Aqui, selecionamos o elemento [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html). Em seguida, chamamos sua função [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener), passando o nome do evento a ser escutado (`'click'`) e uma função para ser executada quando o evento acontecer.

A função que acabamos de passar para `addEventListener()` aqui é chamada de _função anônima_, porque não tem um nome. Há uma maneira alternativa de escrever funções anônimas, que chamamos de _arrow function_ (função de seta).
Uma função de seta usa `() =>` em vez de `function ()`:

```js
document.querySelector("html").addEventListener("click", () => {
  alert("Ai! Pare de me cutucar!");
});
```

> Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
