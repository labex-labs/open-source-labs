# Sobreposição de Texto em Imagem

`index.html` e `style.css` já foram fornecidos na VM.

Para exibir texto sobre uma imagem com uma sobreposição, use a propriedade `backdrop-filter` para aplicar um efeito de `blur(14px)` e `brightness(80%)`. Isso garante que o texto seja legível, independentemente da imagem de fundo e da cor. Aqui está um exemplo de código HTML:

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

E o código CSS correspondente:

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
