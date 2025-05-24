# Deletar Branches Detached (Desanexados)

Você tem um repositório Git com vários branches detached (desanexados) que você não precisa mais. Esses branches estão desorganizando seu repositório e dificultando o gerenciamento. Você deseja deletar todos os branches detached para limpar seu repositório.

Para completar este laboratório, você usará o repositório Git `git-playground` da sua conta GitHub, que vem de um fork de `https://github.com/labex-labs/git-playground.git`. Não marque "Copy the master branch only" (Copiar apenas o branch master).

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Como existe um branch `feature-branch` no repositório remoto, alterne para `feature-branch`, o que fará com que o `feature-branch` local rastreie o branch `feature-branch` do repositório remoto e delete o branch `feature-branch` no repositório remoto:

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. Visualize a relação de rastreamento entre os branches locais e os branches remotos que eles rastreiam:

```shell
git branch -vv
```

4. Volte para o branch `master`:

```shell
git checkout master
```

5. Remova todos os branches detached do seu repositório local:

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. Verifique se os branches detached foram deletados:

```shell
git branch
```

A saída deve mostrar apenas os branches que estão associados a um branch específico:

```shell
* master d22f46b [origin/master] Added file2.txt
```
