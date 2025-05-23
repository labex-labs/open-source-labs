# インタラクティブな再ベースを行う

開発者チームと共同作業しているプロジェクトに取り組んでおり、自分のブランチにいくつかのコミットを行ってきました。しかし、いくつかのコミットは不要であることや、結合する必要があることに気づきました。コミット履歴を整理し、もっと整然としたものにしたいと思っています。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。以下の手順に従ってください。

1. ディレクトリに移動します。
   ```shell
   cd git-playground
   ```
2. 最後の 2 つのコミットのインタラクティブな再ベースを行います。
   ```shell
   git rebase -i HEAD~2
   ```
   インタラクティブな再ベースファイルが既定のテキストエディタで開きます。コミットの順序と、それぞれに対して実行するアクション（pick、squash、drop、reword など）を変更できます。
3. コミットメッセージ「Added file2.txt」の中で「pick」を「squash」に変更し、<kbd>Esc</kbd> キーを押して <kbd>:wq</kbd> コマンドを入力し、その後 <kbd>Enter</kbd> キーを押して変更を保存してエディタを終了し、同じ方法でコミットメッセージを「Added file1.txt and file2.txt」に変更して終了します。
4. マージコンフリクトが発生した場合や変更が必要な場合は、準備ができたら `git rebase --continue` を使用して再ベースを続けるか、`git rebase --abort` を使用して中止することができます。

`git log` を実行すると、次のような結果が得られます。

```shell
[object Object]
```
