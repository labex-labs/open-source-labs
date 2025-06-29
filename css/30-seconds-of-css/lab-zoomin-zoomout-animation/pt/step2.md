# Estilização CSS Básica

Agora que temos nossa estrutura HTML em vigor, vamos criar a estilização CSS básica para o nosso elemento de animação.

1. Abra o arquivo `style.css` no editor.

2. Se o arquivo estiver vazio ou ausente, crie-o com o seguinte conteúdo:

```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
}

.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
}
```

3. Vamos entender o que este CSS faz:
   - Definimos alguma estilização básica para a página (fonte, largura e margens)
   - Estilizamos o cabeçalho com uma cor cinza escuro
   - Para o nosso elemento de animação `.zoom-in-out-box`, nós:
     - Adicionamos uma margem de 24px ao redor dele
     - Definimos sua largura e altura para 50px
     - Damos a ele uma cor de fundo rosa vibrante

4. Salve o arquivo `style.css` após fazer essas alterações.

5. Para ver seu progresso, clique no botão "Go Live" no canto inferior direito do VSCode. Isso iniciará um servidor web na porta 8080. Em seguida, atualize a aba **Web 8080** para ver sua caixa estilizada.

Você deve ver agora um pequeno quadrado rosa em sua página web. Este quadrado é o elemento que animaremos nos próximos passos.
