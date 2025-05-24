# Donut Spinner (Carregador de Donut)

`index.html` e `style.css` já foram fornecidos na VM.

Para indicar o carregamento de conteúdo, crie um carregador de donut (donut spinner) com uma `border` semi-transparente para todo o elemento. Exclua um lado para servir como o indicador de carregamento do donut. Em seguida, defina e use uma animação apropriada, usando `transform: rotate()` para rotacionar o elemento. Aqui está um exemplo de código em HTML e CSS:

HTML:

```html
<div class="donut"></div>
```

CSS:

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
