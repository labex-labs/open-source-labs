# Animação de Balanço em Botão

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de balanço ao focar, você deve usar uma `transition` apropriada para animar as mudanças no elemento. Em seguida, aplique a pseudo-classe `:focus` ao elemento e use `animation` com `transform` para fazê-lo balançar. Finalmente, adicione `animation-iteration-count` para reproduzir a animação apenas uma vez. Aqui está um exemplo de como fazer isso em HTML e CSS:

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
