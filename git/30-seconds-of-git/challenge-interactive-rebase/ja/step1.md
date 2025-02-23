# インタラクティブなリベースを行う

開発者チームと共同作業をしているプロジェクトに取り組んでおり、自分のブランチにいくつかのコミットを行ってきました。しかし、いくつかのコミットは不要であることや、結合する必要があることに気づきました。コミット履歴を整理し、もっと整然としたものにしたいと思っています。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. ディレクトリに移動します。
2. 最後の 2 つのコミットのインタラクティブなリベースを行います。
3. コミットメッセージ「Added file2.txt」の中で「pick」を「squash」に変更し、<kbd>Esc</kbd> キーを押して <kbd>:wq</kbd> コマンドを入力し、次に <kbd>Enter</kbd> キーを押して変更を保存してエディタを終了し、同じ方法でコミットメッセージを「Added file1.txt and file2.txt」に変更して終了します。

`git log` を実行すると、次のような結果が得られます。

```shell
commit 7575ded485555c28ecb09487c68e90639bebbe9d (HEAD -> master)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt and file2.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
