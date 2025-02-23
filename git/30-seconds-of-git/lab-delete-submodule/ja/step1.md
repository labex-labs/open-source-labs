# サブモジュールの削除

`sha1collisiondetection` という名前のサブモジュールを含む Git リポジトリがあります。このサブモジュールをリポジトリから削除したいと思います。

この実験では、`https://github.com/git/git` という名前の Git リポジトリを使用します。このリポジトリには `sha1collisiondetection` という名前のサブモジュールが含まれています。

リポジトリから `sha1collisiondetection` サブモジュールを削除するには、次の手順に従います。

1. ターミナルを開き、Git リポジトリのルートディレクトリに移動します。
   ```
   cd git
   ```
2. 次のコマンドを実行して、`sha1collisiondetection` サブモジュールを登録解除します。
   ```
   git submodule deinit -f -- sha1collisiondetection
   ```
3. 次のコマンドを実行して、`sha1collisiondetection` サブモジュールのディレクトリを削除します。
   ```
   rm -rf.git/modules/sha1collisiondetection
   ```
4. 次のコマンドを実行して、`sha1collisiondetection` サブモジュールのワーキングツリーを削除します。
   ```
   git rm -f sha1collisiondetection
   ```

これらの手順を実行すると、`sha1collisiondetection` サブモジュールが Git リポジトリから削除されます。`git submodule status` コマンドを実行すると、サブモジュールに関する情報は表示されません。
