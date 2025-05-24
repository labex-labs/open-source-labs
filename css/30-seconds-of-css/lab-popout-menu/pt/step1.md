# Menu Popout

`index.html` e `style.css` já foram fornecidos na VM.

Para revelar um menu popout interativo ao passar o mouse (hover) ou ao receber foco (focus), siga estes passos:

1.  Use `left: 100%` no CSS para posicionar o menu popout à direita do elemento pai.
2.  Use `visibility: hidden` em vez de `display: none` para ocultar o menu popout inicialmente, permitindo que as transições sejam aplicadas.
3.  Aplique os seletores de pseudo-classe `:hover`, `:focus` e `:focus-within` ao elemento pai para exibir o menu popout quando ele estiver com o mouse sobre (hover) ou em foco (focus).
4.  Use o seguinte código HTML e CSS:

HTML:

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS:

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover > .popout-menu,
.reference:focus > .popout-menu,
.reference:focus-within > .popout-menu {
  visibility: visible;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
