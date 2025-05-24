# Barra de Progresso de Rolagem

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma barra de progresso que mostra a porcentagem de rolagem de uma página da web, siga estas etapas:

1.  Adicione um elemento `div` com o `id` "scroll-progress" ao código HTML.
2.  No código CSS, defina a `position` do elemento como `fixed`, o `top` como `0`, a `width` como `0%`, a `height` como `4px` e a cor de `background` como `#7983ff`.
3.  Defina o valor de `z-index` para um número grande para garantir que a barra de progresso seja colocada no topo da página e acima de qualquer conteúdo.
4.  No código JavaScript, selecione o elemento `scroll-progress` usando o método `document.getElementById()`.
5.  Calcule a altura da página da web usando a fórmula `document.documentElement.scrollHeight - document.documentElement.clientHeight`.
6.  Adicione um ouvinte de evento (event listener) ao objeto `window` que escuta o evento `scroll`.
7.  Na função do ouvinte de evento, calcule a porcentagem de rolagem do documento usando a fórmula `(scrollTop / height) * 100`.
8.  Defina a `width` do elemento `scroll-progress` para a porcentagem de rolagem usando a propriedade `style`.

Aqui está o código:

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
