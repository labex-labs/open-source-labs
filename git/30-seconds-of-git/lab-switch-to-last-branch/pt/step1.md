# Retornar para a Branch Anterior

Como desenvolvedor, você está trabalhando em um projeto e mudou para uma branch diferente para trabalhar em uma nova funcionalidade. Depois de fazer algumas alterações, você percebe que precisa voltar para a branch anterior para corrigir um bug. Você pode commitar (confirmar) suas alterações em uma nova branch e usar um comando para alternar rapidamente para a branch anterior.

Para demonstrar como voltar para a branch anterior, usaremos o repositório Git chamado `https://github.com/labex-labs/git-playground`. Siga os passos abaixo:

1. Clone o repositório usando o seguinte comando:
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Mude para o diretório do repositório:
   ```
   cd git-playground
   ```
3. Crie uma nova branch chamada `feature-branch`:
   ```
   git checkout -b feature-branch
   ```
4. Verifique a branch atual e alterne rapidamente para a branch anterior. O nome da sua nova branch é `feature-branch` e o nome da branch anterior para a qual você deseja voltar é `master`:
   ```
   git checkout -
   ```
   Isso irá alternar de volta para a branch `master`, e suas alterações ainda estarão lá.
