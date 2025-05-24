# Mostrar Conteúdo Adicional ao Passar o Mouse (Hover)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um cartão que exibe conteúdo adicional ao passar o mouse (hover), siga estes passos:

1.  Use `overflow: hidden` no cartão para ocultar quaisquer elementos que transbordem verticalmente.
2.  Use os seletores de pseudo-classe `:hover` e `:focus-within` para alterar o estilo do cartão quando o elemento estiver com o mouse sobre, focado ou qualquer um de seus descendentes estiver focado.
3.  Defina `transition: 0.3s ease all` para criar um efeito de transição suave ao passar o mouse/focar.

Aqui está um exemplo de código HTML para o cartão:

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link to source</a>
    </p>
  </div>
</div>
```

E aqui está o código CSS para estilizar o cartão:

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card .focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
