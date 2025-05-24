# Texto Alternado

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de texto alternado, siga estes passos:

1. Crie um elemento `<span>` com a classe "alternating" e um `id` de "alternating-text" para conter o texto que será alternado:

```html
<p>
  Eu amo programar em <span class="alternating" id="alternating-text"></span>.
</p>
```

2. No CSS, defina uma animação chamada `alternating-text` que fará com que o elemento `<span>` desapareça, definindo `display: none`:

```css
.alternating {
  animation-name: alternating-text;
  animation-duration: 3s;
  animation-iteration-count: infinite;
  animation-timing-function: ease;
}

@keyframes alternating-text {
  90% {
    display: none;
  }
}
```

3. Em JavaScript, defina um array das diferentes palavras que serão alternadas e use a primeira palavra para inicializar o conteúdo do elemento `<span>`:

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating-text");

let i = 0;
element.innerHTML = texts[0];
```

4. Use `EventTarget.addEventListener()` para definir um ouvinte de evento para o evento `'animationiteration'`. Isso executará o manipulador de eventos sempre que uma iteração da animação for concluída. No manipulador de eventos, use `Element.innerHTML` para exibir o próximo elemento no array `texts` como o conteúdo do elemento `<span>`:

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
