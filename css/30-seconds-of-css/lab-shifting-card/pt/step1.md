# Cartão Deslocável (Shifting Card)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um cartão que se desloca ao passar o mouse, siga estes passos:

1.  Defina a propriedade `perspective` apropriada no elemento `.container` para permitir o efeito de deslocamento.
2.  Adicione uma `transition` para a propriedade `transform` do elemento `.card`.
3.  Use `Document.querySelector()` para selecionar o elemento `.card` e adicione ouvintes de eventos (event listeners) para os eventos `mousemove` e `mouseout`.
4.  Use `Element.getBoundingClientRect()` para obter os valores `x`, `y`, `width` e `height` do elemento `.card`.
5.  Calcule a distância relativa como um valor entre `-1` e `1` para os eixos `x` e `y` e aplique-a através da propriedade `transform`.

Aqui está o código HTML e CSS de exemplo para o cartão:

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>Card</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti
        repellat, consequuntur doloribus voluptate esse iure?
      </p>
    </div>
  </div>
</div>
```

```css
.container {
  display: flex;
  padding: 24px;
  justify-content: center;
  align-items: center;
  background: #f3f1fe;
  perspective: 1000px;
}

.shifting-card {
  width: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  margin: 0.5rem;
  transition: transform 0.2s ease-out;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.shifting-card .content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

E aqui está o código JavaScript para adicionar o efeito de hover:

```js
const card = document.querySelector(".shifting-card");
const { x, y, width, height } = card.getBoundingClientRect();
const cx = x + width / 2;
const cy = y + height / 2;

const handleMove = (e) => {
  const { pageX, pageY } = e;
  const dx = (cx - pageX) / (width / 2);
  const dy = (cy - pageY) / (height / 2);
  e.target.style.transform = `rotateX(${10 * dy * -1}deg) rotateY(${
    10 * dx
  }deg)`;
};

const handleOut = (e) => {
  e.target.style.transform = "initial";
};

card.addEventListener("mousemove", handleMove);
card.addEventListener("mouseout", handleOut);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
