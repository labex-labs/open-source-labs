# Fazer Merge de uma Branch

Sua tarefa é fazer merge (merge) de uma branch na branch atual usando Git. Você precisará mudar para a branch de destino e, em seguida, fazer merge da branch de origem nela. Isso pode ser útil quando você deseja combinar as alterações de uma branch `feature-branch-A` na branch `master` do seu projeto.

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga estas etapas para fazer merge da `feature-branch-A` na branch `master`:

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "seu-nome-de-usuário"
git config --global user.email "seu-email"
```

2. Crie uma branch `feature-branch-A`. Mude para ela:

```shell
git checkout -b feature-branch-A
```

3. Adicione "hello,world" ao arquivo `file2.txt`, adicione-o à área de staging (staging area) e faça o commit com a mensagem "fix file2.txt":

```shell
echo "hello,world" >> file2.txt
git add .
git commit -m "fix file2.txt"
```

4. Mude para a branch `master`:

```shell
git checkout master
```

5. Faça merge da `feature-branch-A` na branch `master`:

```shell
git merge feature-branch-A
```

6. Resolva quaisquer conflitos que possam surgir durante o processo de merge.

Este é o resultado da execução de `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
