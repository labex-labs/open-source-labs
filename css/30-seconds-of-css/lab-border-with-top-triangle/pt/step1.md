# Borda com Triângulo Superior

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um contêiner de conteúdo com um triângulo no topo, siga estes passos:

1. Use os pseudo-elementos `::before` e `::after` para criar dois triângulos.
2. Defina a `border-color` e a `background-color` dos triângulos para corresponder ao contêiner.
3. Defina a `border-width` do triângulo `::before` para ser `1px` mais largo que o triângulo `::after` para atuar como a borda.
4. Posicione o triângulo `::after` `1px` à direita do triângulo `::before` para permitir que a borda esquerda seja exibida.

Aqui está um exemplo de código HTML para o contêiner:

```html
<div class="container">Border with top triangle</div>
```

E aqui está o código CSS correspondente:

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
