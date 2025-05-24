# Bouncing Loader (Carregador com Efeito de Salto)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de carregamento com efeito de salto:

1.  Defina uma animação `@keyframes` que usa as propriedades `opacity` e `transform`, com uma translação em um único eixo em `transform: translate3d()` para melhor desempenho.
2.  Crie um contêiner pai com a classe `.bouncing-loader` que usa `display: flex` e `justify-content: center` para centralizar os círculos com efeito de salto.
3.  Dê aos três elementos `<div>` para os círculos com efeito de salto a mesma `width`, `height` e `border-radius: 50%` para torná-los circulares.
4.  Aplique a animação `bouncing-loader` a cada um dos três círculos com efeito de salto.
5.  Use um `animation-delay` diferente para cada círculo e `animation-direction: alternate` para criar o efeito apropriado.

Aqui está o código HTML:

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

E aqui está o código CSS:

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
