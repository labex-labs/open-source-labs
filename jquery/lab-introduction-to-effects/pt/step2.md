# Alterando a Exibição com Base no Estado de Visibilidade Atual

O jQuery também pode permitir que você altere a visibilidade de um conteúdo com base em seu estado de visibilidade atual. `.toggle()` mostrará o conteúdo que está atualmente oculto e ocultará o conteúdo que está atualmente visível. Você pode passar os mesmos argumentos para `.toggle()` que você passa para qualquer um dos métodos de efeitos acima.

```js
// Alternar instantaneamente a exibição de todos os parágrafos
$("p").toggle();

// Alternar a exibição de todas as divs em 1,8 segundos
$("div").toggle(1800);
```

`.toggle()` usará uma combinação de efeitos de slide e fade, assim como `.show()` e `.hide()` fazem.

> Você pode atualizar a aba **Web 8080** para visualizar a página web.
