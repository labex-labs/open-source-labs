# Rotação de Imagem ao Passar o Mouse (Hover)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um efeito de rotação para uma imagem ao passar o mouse (hover), use as propriedades `scale()`, `rotate()` e `transition` ao passar o mouse sobre o elemento pai, que deve ser um elemento `<figure>`. Para garantir que a transformação da imagem não transborde do elemento pai, adicione `overflow: hidden` ao CSS do elemento pai. Aqui está um exemplo de código HTML e CSS:

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
