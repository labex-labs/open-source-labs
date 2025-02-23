# 特定の文字列を操作したコミットを見つける

開発者として、コードベース内の特定の文字列を変更したすべてのコミットを見つける必要がある場合があります。たとえば、特定の関数名や変数を追加または削除したすべてのコミットを見つけたい場合があります。これは、問題のデバッグやバグの原因を追跡する際に役立ちます。

GitHub 上にホストされている `git-playground` という名前のプロジェクトを作業しているとしましょう。`README.md` ファイル内の文字列 "Git Playground" を変更したすべてのコミットを見つけたいと思います。以下がその方法です。

1. リポジトリディレクトリに移動します。

```shell
cd git-playground
```

2. `git log -S` コマンドを使用して、`README.md` ファイル内の文字列 "Git Playground" を変更したすべてのコミットを見つけ、矢印キーを使用してコミットの一覧を表示します。ログを終了するには <kbd>Q</kbd> キーを押します。

```shell
git log -S"Git Playground" README.md
```

Git は、`README.md` ファイル内の文字列 "Git Playground" を変更したすべてのコミットの一覧を出力します。

```shell
commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
