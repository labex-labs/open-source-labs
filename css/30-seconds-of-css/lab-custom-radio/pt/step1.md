# Botão de Rádio Personalizado

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um botão de rádio estilizado com animação na mudança de estado, siga estes passos:

1.  Crie um `.radio-container` usando flexbox para criar o layout apropriado para os botões de rádio.
2.  Resete os estilos no `<input>` e use-o para criar o contorno e o fundo do botão de rádio.
3.  Use o elemento `::before` para criar o círculo interno do botão de rádio.
4.  Crie um efeito de animação na mudança de estado usando `transform: scale(1)` e uma transição CSS.

Aqui está um exemplo de trecho HTML:

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Apples</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Oranges</label>
</div>
```

E aqui está o CSS correspondente:

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
