# リモートから最新の変更を取得する

開発チームでプロジェクトを行っており、そのプロジェクトがリモート リポジトリに保存されているとしましょう。ローカル リポジトリに適用せずに、リモート リポジトリから最新の変更を取得したい場合があります。このときに便利なのが `git fetch` コマンドです。

`git fetch` コマンドは、リモート リポジトリから最新の変更をダウンロードしてローカル リポジトリに保存しますが、作業ディレクトリには適用しません。つまり、ローカル リポジトリにマージする前に変更を確認できます。

リモート リポジトリから最新の変更を取得する方法を示すために、GitHub アカウントの Git リポジトリ `git-playground` を使用します。これは `https://github.com/labex-labs/git-playground.git` のフォークから来ています。以下の手順に従ってください。

1. リポジトリをクローンし、ディレクトリに移動します。

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Github サイトのアカウント内で `git-playground` リポジトリを見つけ、`fetch-branch` という名前のブランチを作成して切り替え、`hello.txt` という名前のファイルを作成し、"hello, world" を追加して "Create hello.txt" というメッセージでコミットします。
3. リモート リポジトリのブランチを表示します。

```shell
git branch -r
```

4. リモート リポジトリから最新の変更を取得します。

```shell
git fetch
```

5. 再度、リモート リポジトリのブランチを表示し、最新の変更が取得されたことを確認します。

```shell
git branch -r
git log origin/fetch-branch
```

これにより、`origin/fetch-branch` ブランチの最新コミットが表示されます。これが `git log origin/fetch-branch` を実行した結果です。

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
