# Resetar o Branch Master Local para Corresponder ao Remoto

Você tem trabalhado em um projeto e fez alterações no branch `master` local. No entanto, você percebe que o branch `master` remoto foi atualizado com novas alterações que você não possui em seu branch local. Você precisa resetar o branch `master` local para corresponder ao do remoto.

1. Mude para o branch `master`:
   ```shell
   git checkout master
   ```
2. Recupere as últimas atualizações do remoto:
   ```shell
   git fetch origin
   ```
3. Visualize o histórico de commits do branch atual:
   ```shell
   git log
   ```
4. Resete o branch `master` local para corresponder ao do remoto:
   ```shell
   git reset --hard origin/master
   ```
5. Verifique se o branch `master` local está agora atualizado com o branch `master` remoto:
   ```shell
   git log
   ```

Este é o resultado final:

```shell
[object Object]
```
