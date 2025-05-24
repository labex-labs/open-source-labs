# Efeito de Máquina de Escrever (Typewriter Effect)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma animação de efeito de máquina de escrever, siga estes passos:

1.  Defina duas animações, `typing` e `blink`. `typing` anima os caracteres, e `blink` anima o cursor (caret).
2.  Use o pseudo-elemento `::after` para adicionar o cursor ao elemento container.
3.  Use JavaScript para definir o texto para o elemento interno e definir a variável `--characters`, que contém a contagem de caracteres. Esta variável é usada para animar o texto.
4.  Use `white-space: nowrap` e `overflow: hidden` para tornar o conteúdo invisível conforme necessário.

Aqui está o código HTML:

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

E aqui está o código CSS:

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

E, finalmente, aqui está o código JavaScript:

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
