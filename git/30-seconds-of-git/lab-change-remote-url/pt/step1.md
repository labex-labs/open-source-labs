# Alterar a URL Remota

Você clonou um repositório do GitHub e fez algumas alterações nele. No entanto, agora percebe que precisa alterar a URL do repositório remoto. Isso pode ser porque o repositório original foi movido para um local diferente, ou porque você deseja enviar suas alterações para um repositório remoto diferente. Sua tarefa é alterar a URL remota do repositório usando comandos Git.

Você precisará clonar o repositório `https://github.com/labex-labs/git-playground` para sua máquina local. Para alterar a URL remota do repositório para `https://github.com/your-username/git-playground`, siga estas etapas:

1. Abra um terminal ou prompt de comando, clone o repositório e navegue até o repositório local.
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. Use o seguinte comando para visualizar a URL remota atual:
   ```
   git remote -v
   ```
3. Use o seguinte comando para alterar a URL remota para a nova URL:
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. Use o seguinte comando para verificar se a URL remota foi alterada:
   ```
   git remote -v
   ```

A saída deve mostrar a nova URL em vez da antiga:

![Updated remote URL output](../assets/challenge-change-remote-url-step1-1.png)
