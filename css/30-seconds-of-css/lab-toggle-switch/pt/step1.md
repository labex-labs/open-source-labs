# Interruptor de Alternância (Toggle Switch)

`index.html` e `style.css` já foram fornecidos na VM.

Aqui está uma versão mais concisa e clara do conteúdo:

Para criar um interruptor de alternância (toggle switch) apenas com CSS, siga estes passos:

1.  Associe o `<label>` com o elemento de caixa de seleção `<input>` usando o atributo `for`.
2.  Use o pseudo-elemento `::after` do `<label>` para criar um botão circular para o interruptor.
3.  Use o seletor de pseudo-classe `:checked` para alterar a posição do botão, usando `transform: translateX(20px)` e o `background-color` do interruptor.
4.  Oculte visualmente o elemento `<input>` usando `position: absolute` e `left: -9999px`.

Aqui está o código HTML:

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

Aqui está o código CSS:

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
