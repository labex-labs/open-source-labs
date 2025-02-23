# git のテキストエディタを構成する

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。Git が使用するテキストエディタを好きなエディタに構成したいと思います。

1. `git-playground` リポジトリをクローンします。

```shell
git clone https://github.com/labex-labs/git-playground
```

2. クローンしたリポジトリに移動して ID を構成します。

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Git に好きなテキストエディタを使用するように構成します (この例では vim を使用します)。

```shell
git config --global core.editor "vim"
```

4. ファイルを変更してコミット用にステージングします。

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. 変更をコミットします。

```shell
git commit
```

6. 好きなテキストエディタ (この例では vim) がコミットメッセージ付きで開きます。コミットメッセージ "Update hello.txt" を書き込んでファイルを保存します。
7. テキストエディタを閉じます。書いたメッセージでコミットが行われます。

これが完成した結果です。

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
