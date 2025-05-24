# Imagem com Sobreposição de Texto

`index.html` e `style.css` já foram fornecidos na VM.

Para exibir uma imagem com uma sobreposição de texto, use os elementos `<figure>` e `<figcaption>`. Use a propriedade `linear-gradient` em CSS para criar o efeito de sobreposição sobre a imagem. Aqui está um exemplo de trecho de código:

```html
<figure class="text-overlay-image">
  <img src="https://picsum.photos/id/971/400/400.jpg" />
  <figcaption>
    <h3>Business <br />Pricing</h3>
  </figcaption>
</figure>
```

```css
.text-overlay-image {
  box-sizing: border-box;
  position: relative;
  margin: 8px;
  max-width: 400px;
  max-height: 400px;
  width: 100%;
}

.text-overlay-image figcaption {
  box-sizing: border-box;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: linear-gradient(0deg, #00000088 30%, #ffffff44 100%);
  color: #fff;
  padding: 16px;
  font: 700 28px/1.2 sans-serif;
}

.text-overlay-image figcaption h3 {
  margin: 0;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
