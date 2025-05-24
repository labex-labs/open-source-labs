# Sublinhado de Texto Elegante

`index.html` e `style.css` já foram fornecidos na VM.

Para evitar que os descendentes cortem o sublinhado, use `text-shadow` com quatro valores para criar uma sombra espessa que cubra a linha onde os descendentes encontram o sublinhado. Certifique-se de que a cor do `text-shadow` corresponda à cor do `background` e ajuste os valores em `px` para fontes maiores. Crie o sublinhado real usando `background-image` com um `linear-gradient()` e `currentColor`. Defina `background-position`, `background-repeat` e `background-size` para colocar o gradiente na posição correta. Use o seletor de pseudo-classe `::selection` para garantir que a sombra do texto não interfira na seleção do texto. Observe que este efeito é implementado nativamente como `text-decoration-skip-ink: auto`, mas tem menos controle sobre o sublinhado.

Aqui está um exemplo de trecho de código:

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
