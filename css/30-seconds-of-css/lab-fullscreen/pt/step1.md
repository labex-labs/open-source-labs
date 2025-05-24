# Tela Cheia (Fullscreen)

`index.html` e `style.css` já foram fornecidos na VM.

Para estilizar um elemento em modo de tela cheia (fullscreen), você pode usar o seletor de pseudo-elemento CSS `:fullscreen`. Você também pode criar um botão que torna o elemento em tela cheia para fins de visualização usando um `<button>` e `Element.requestFullscreen()`. Aqui está um exemplo de código:

```html
<div class="container">
  <p>
    <em
      >Clique no botão abaixo para entrar com o elemento em modo de tela cheia.
    </em>
  </p>
  <div class="element" id="element">
    <p>Eu mudo de cor no modo de tela cheia!</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    Ir para Tela Cheia!
  </button>
</div>
```

```css
.container {
  margin: 40px auto;
  max-width: 700px;
}

.element {
  padding: 20px;
  height: 300px;
  width: 100%;
  background-color: skyblue;
  box-sizing: border-box;
}

.element p {
  text-align: center;
  color: white;
  font-size: 3em;
}

/* For Internet Explorer */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* For modern browsers */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
