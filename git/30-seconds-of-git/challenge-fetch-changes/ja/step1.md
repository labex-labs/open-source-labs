# リモートから最新の変更を取得する

開発チームでプロジェクトを行っており、そのプロジェクトがリモート リポジトリに保存されているとします。ローカル リポジトリに適用せずに、リモート リポジトリから最新の変更を取得したいと思います。

## タスク

リモート リポジトリから最新の変更を取得する方法を示すために、GitHub アカウントの Git リポジトリ `git-playground` を使用します。これは、`https://github.com/labex-labs/git-playground.git` のフォークから来ています。

1. リポジトリをクローンし、ディレクトリに移動します。
2. Github ウェブサイトのアカウント内で `git-playground` リポジトリを見つけ、`fetch-branch` と呼ばれるブランチを作成して切り替え、`hello.txt` と呼ばれるファイルを作成し、「hello, world」を追加して「Create hello.txt」というメッセージでコミットします。
3. リモート リポジトリ内のブランチを表示します。
4. リモート リポジトリから最新の変更を取得します。
5. 再度、リモート リポジトリ内のブランチを表示し、最新の変更が取得されたことを確認します。

これが `git log origin/fetch-branch` を実行した結果です。

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
