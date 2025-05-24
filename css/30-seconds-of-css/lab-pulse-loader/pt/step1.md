# Carregador de Pulsação (Pulse Loader)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de carregamento com efeito de pulsação usando a propriedade `animation-delay`, siga estes passos:

1.  Use `@keyframes` para definir uma animação para dois elementos `<div>`. Defina o ponto de partida (`0%`) para ambos os elementos sem `width` ou `height` e posicione-os no centro. Para o ponto final (`100%`), faça com que ambos os elementos aumentem em `width` e `height`, mas reinicie sua `position` para `0`.
2.  Use `opacity` para fazer a transição de `1` para `0` ao animar, para dar aos elementos `<div>` um efeito de desaparecimento à medida que se expandem.
3.  Defina um `width` e `height` predefinidos para o contêiner pai, `.ripple-loader`. Use `position: relative` para posicionar seus filhos.
4.  Use `animation-delay` no segundo elemento `<div>`, para que cada elemento inicie sua animação em um tempo diferente.

Aqui está o código HTML e CSS para conseguir isso:

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
