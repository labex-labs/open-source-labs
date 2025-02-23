# 上流ブランチ作成の自動化

開発者として、プッシュ時に上流ブランチを作成するプロセスを自動化したいと考えています。これにより、リモートリポジトリで手動でブランチを作成する面倒を避けることができます。

## タスク

このチャレンジを完了するには、GitHub アカウント内の Git リポジトリ `git-playground` を使用して、`https://github.com/labex-labs/git-playground.git` のフォークからプッシュ時に自動的に上流ブランチを作成します。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。
2. プッシュ時に自動的な上流ブランチ作成を有効にします。
3. `new-feature` と呼ばれるブランチを作成して切り替え、`hello.txt` ファイルを追加してその中に "hello,world" を書き込み、ステージングエリアに追加して "Added hello.txt" というメッセージでコミットします。
4. 変更を `new-feature` と呼ばれる新しいブランチにプッシュします。このブランチはリモートリポジトリには存在しません。

これがチャレンジを完了した後の結果です。

![automatic upstream branch result](../assets/challenge-automatic-push-upstream-step1-1.png)
