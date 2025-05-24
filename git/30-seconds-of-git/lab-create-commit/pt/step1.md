# Criar um Commit Git

Você fez algumas alterações em seu código e deseja salvá-las como um snapshot em seu repositório Git. No entanto, você não quer salvar todas as alterações que fez, apenas aquelas que são relevantes para a funcionalidade atual ou correção de bug. Como você pode criar um commit contendo apenas as alterações relevantes?

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`, siga estes passos:

1. Clone o repositório e navegue até ele:

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. Configure sua conta do GitHub no ambiente:

   ```
   git config --global user.name "your-name"
   git config --global user.email "your-email"
   ```

3. Adicione "hello,labex" ao arquivo `README.md`, adicione-o à área de staging (staging area) e faça o commit com a mensagem "Update README.md":

   ```
   echo "hello,labex" >> README.md
   git add .
   git commit -m "Update README.md"
   ```

   A opção `-m` permite que você especifique uma mensagem de commit. Certifique-se de que a mensagem seja descritiva e explique quais alterações o commit contém.

Este é o resultado da execução do comando `git log`:

![git log command output](../assets/challenge-create-commit-step1-1.png)
