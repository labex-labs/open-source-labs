# Ajustar Imagem no Contêiner

`index.html` e `style.css` já foram fornecidos na VM.

Para ajustar uma imagem dentro de seu contêiner, preservando sua proporção, você pode usar `object-fit: contain`. Para preencher o contêiner com a imagem, preservando sua proporção, use `object-fit: cover`. Se você deseja posicionar a imagem no centro do contêiner, pode usar `object-position: center`.

Aqui está um exemplo de como você pode usar essas propriedades:

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

E o CSS correspondente:

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
