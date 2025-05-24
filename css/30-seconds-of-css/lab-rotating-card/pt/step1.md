# Cartão Rotativo

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um cartão de duas faces que rotaciona ao passar o mouse (hover), siga estes passos:

1.  Defina a propriedade `backface-visibility` dos cartões como `none` para evitar que a parte de trás seja visível por padrão.
2.  Inicialmente, defina `rotateY(-180deg)` para a parte de trás do cartão e `rotateY(0deg)` para a parte da frente do cartão.
3.  Ao passar o mouse (hover), defina `rotateY(180deg)` para a parte da frente do cartão e `rotateY(0deg)` para a parte de trás do cartão.
4.  Defina o valor `perspective` apropriado para criar o efeito de rotação.

Aqui está um exemplo de código HTML e CSS:

```html
<div class="card">
  <div class="card-side front">
    <div>Front Side</div>
  </div>
  <div class="card-side back">
    <div>Back Side</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover .card-side.front {
  transform: rotateY(180deg);
}

.card:hover .card-side.back {
  transform: rotateY(0deg);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
