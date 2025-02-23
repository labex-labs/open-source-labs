# Configure the git text editor

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Vous voulez configurer l'éditeur de texte utilisé par Git pour votre éditeur préféré.

1. Clonez le référentiel `git-playground` :

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Accédez au référentiel cloné et configurez l'identité :

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Configurez Git pour utiliser votre éditeur de texte préféré (dans cet exemple, nous utiliserons vim) :

```shell
git config --global core.editor "vim"
```

4. Apportez une modification à un fichier et préparez-le pour le commit :

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. Validez la modification :

```shell
git commit
```

6. Votre éditeur de texte préféré (dans cet exemple, vim) devrait s'ouvrir avec le message de commit. Notez votre message de commit "Update hello.txt" et enregistrez le fichier.
7. Fermez l'éditeur de texte. Le commit sera effectué avec le message que vous avez écrit.

Voici le résultat final :

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
