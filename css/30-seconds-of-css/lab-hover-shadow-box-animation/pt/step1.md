# Animação de Sombra Hover (Hover Shadow Box Animation)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma caixa de sombra ao redor do texto quando ele estiver em hover (hovered), siga estes passos:

1. Defina `transform: perspective(1px)` para dar ao elemento um espaço 3D, afetando a distância entre o plano Z e o usuário, e `translateZ(0)` para reposicionar o elemento `p` ao longo do eixo z no espaço 3D.
2. Use `box-shadow` para tornar a caixa transparente.
3. Habilite as transições para `box-shadow` e `transform` usando a propriedade `transition-property`.
4. Aplique um novo `box-shadow` e `transform: scale(1.2)` para alterar a escala do texto usando os seletores de pseudo-classe `:hover`, `:active` e `:focus`.
5. Adicione a classe `hover-shadow-box-animation` ao elemento `p`.

Aqui está o código HTML:

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

E aqui está o código CSS:

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
