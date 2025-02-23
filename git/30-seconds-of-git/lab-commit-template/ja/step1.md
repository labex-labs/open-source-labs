# コミットメッセージ テンプレートを追加する

コミットメッセージ テンプレートがない場合、開発者は「バグ修正」や「コード更新」など、漠然とした情報の乏しいコミットメッセージを書こうとする傾向があります。これでは、他の人が変更の目的を理解するのが困難になり、後々混乱やミスにつながる可能性があります。コミットメッセージ テンプレートを設定することで、開発者はより詳細で情報の充実したコミットメッセージを提供するように促され、コラボレーションと生産性が向上します。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。このリポジトリにコミットメッセージ テンプレートを設定するには、次の手順に従ってください。

1. コマンド `git clone https://github.com/labex-labs/git-playground` を使用して、リポジトリをローカル マシンにクローンします。
2. コマンド `cd git-playground` を使用してリポジトリ ディレクトリに移動し、コマンド `git config --global user.name "your-username"` と `git config --global user.email "your-email"` を使用して GitHub アカウントを設定します。
3. コマンド `vim commit-template` を使用して、リポジトリ ディレクトリに新しいファイル `commit-template` を作成します。
4. コミット メッセージ エディタで `commit-template` ファイルを開き、次の行を追加します。

```shell
# <type>: <subject>

# <body>

# <footer>

#これは、3 つのセクションがあるテンプレートを作成します。"<type>" は提出の種類を示し、たとえば "feat" や "fix" で、"<subject>" は提出内容を短く要約したもので、"<body>" はより詳細な説明で、"<footer>" には関連する問題番号やその他のコメントなどの追加メタデータを含めることができます。
```

5. <kbd>Esc</kbd> キーを押して <kbd>:wq</kbd> コマンドを入力し、次に <kbd>Enter</kbd> キーを押して変更を保存し、`commit-template` ファイル エディタを終了します。
6. コマンド `git add commit-template` を使用して、`commit-template` ファイルをステージング エリアに追加します。
7. コマンド `git config commit.template commit-template` を使用して、`commit-template` ファイルをリポジトリのコミットメッセージ テンプレートとして設定します。
8. コマンド `git commit` を使用してコミット メッセージ エディタを開き、コミット メッセージ エディタには、手順 4 で作成したコミットメッセージ テンプレートが含まれていることに注意してください。
9. <kbd>Esc</kbd> キーを押して <kbd>:q</kbd> コマンドを入力し、次に <kbd>Enter</kbd> キーを押してコミット メッセージ エディタを終了します。
