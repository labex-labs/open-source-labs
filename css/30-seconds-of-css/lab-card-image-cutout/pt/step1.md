# Cartão com Recorte de Imagem

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um cartão com um recorte de imagem, siga estes passos:

1.  Adicione um fundo colorido a um elemento `.container` usando a propriedade `background`.
2.  Crie um elemento `.card` e adicione um elemento `figure` dentro dele com a imagem desejada e qualquer outro conteúdo.
3.  Use o pseudo-elemento `::before` para adicionar uma `border` (borda) ao redor do elemento `figure`. Defina a cor da borda para corresponder à cor de `background` do elemento `.container` para criar a ilusão de um recorte no `.card`.

Aqui está um exemplo de código HTML para o cartão:

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

E aqui está o código CSS correspondente:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card .content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
