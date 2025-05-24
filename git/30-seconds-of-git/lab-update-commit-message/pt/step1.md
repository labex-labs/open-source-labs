# Alterar a Mensagem do Último Commit

Imagine que você acabou de commitar algumas alterações em seu repositório Git, mas percebeu que cometeu um erro de digitação na mensagem do commit. Você quer corrigir o erro sem alterar as alterações reais que fez. Como você pode fazer isso?

Para demonstrar como alterar a mensagem do último commit, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga estes passos:

1. Clone o repositório, navegue até o diretório e configure a identidade:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "seu-nome-de-usuário"
   git config --global user.email "seu-email"
   ```
2. Corrija a mensagem do commit do último commit para ler "Fix the network bug" (Corrigir o bug de rede):
   ```
   git commit --amend -m "Fix the network bug"
   ```
   Isso abrirá seu editor de texto padrão onde você poderá modificar a mensagem do commit. Salve e feche o editor para concluir o processo.
3. Verifique se a mensagem do commit foi alterada:
   ```
   git log --oneline
   ```

Você deve ver a mensagem do commit atualizada no log:

```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```
