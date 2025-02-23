# 最後のコミットを表示する

開発チームとともにプロジェクトを行っており、プロジェクトの Git リポジトリに対して行われた最後のコミットを表示する必要があります。コミットメッセージ、作者、日付など、コミットの詳細を確認したいと思っています。

Git リポジトリに対して行われた最後のコミットを表示するには、次の手順に従います。

1. コンピュータのターミナルを開きます。
2. Git リポジトリがあるディレクトリに移動します。

```shell
cd git-playground
```

3. 最後のコミットを表示します。

```shell
git log -1
```

出力には、コミットメッセージ、作者、日付など、最後のコミットの詳細が表示されます。

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
