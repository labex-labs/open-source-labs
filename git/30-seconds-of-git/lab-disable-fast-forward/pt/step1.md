# Desabilitar _Fast Forward Merging_

Por padrão, o Git utiliza o _fast-forward merging_ para mesclar _branches_ que não possuem _commits_ divergentes. Isso significa que, se você tiver uma _branch_ sem novos _commits_, o Git simplesmente moverá o ponteiro da _branch_ que você está mesclando para o último _commit_ da _branch_ da qual você está mesclando. Embora isso possa ser útil em alguns casos, também pode causar problemas, especialmente ao trabalhar em projetos maiores com múltiplos contribuidores. Por exemplo, se dois desenvolvedores estiverem trabalhando na mesma _branch_ e ambos fizerem alterações, o _fast-forward merging_ pode causar conflitos difíceis de resolver.

Para desabilitar o _fast-forward merging_, vamos usar o repositório de `https://github.com/labex-labs/git-playground`.

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Crie e mude para uma _branch_ chamada `my-branch`, crie um arquivo `hello.txt` e adicione "hello,world" a ele, adicione-o à área de _staging_ e faça o _commit_ com a mensagem "Added hello.txt":

```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add .
git commit -m "Added hello.txt"
```

3. Execute o seguinte comando para desabilitar o _fast-forward merging_:

```shell
git config --add merge.ff false
```

Isso desabilitará o _fast-forward merging_ para todas as _branches_, mesmo que seja possível. Você pode usar a flag `--global` para configurar esta opção globalmente:

```shell
git config --global --add merge.ff false
```

4. Volte para a _branch_ `master` e mescle a _branch_ `my-branch`, salve e saia sem alterar o texto:

```shell
git checkout master
git merge my-branch
```

Agora, o Git sempre criará um _merge commit_, mesmo que seja possível fazer _fast forward_:

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch 'my-branch'
```
