# パスカルケース (Pascal case) の理解と環境のセットアップ

パスカルケースは、以下のような命名規則です。

- 各単語の最初の文字は大文字になります。
- 単語間にはスペース、ハイフン、またはアンダースコアは使用されません。
- その他のすべての文字は小文字になります。

例えば：

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

では、開発環境のセットアップから始めましょう。

1. 上部のメニューバーにある「Terminal」をクリックして、WebIDE インターフェイスからターミナルを開きます。

2. ターミナルに以下のコマンドを入力して Enter キーを押し、Node.js の対話型セッションを開始します。

```bash
node
```

Node.js のプロンプト (`>`) が表示され、Node.js の対話型環境に入ったことがわかります。

3. 簡単な文字列操作を試して、準備運動をしましょう。Node.js のプロンプトで以下のコードを入力します。

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

出力は以下のようになるはずです。

```
John doe
```

この簡単な例では、文字列の最初の文字を大文字にする方法を示しています。以下のものを使用しました。

- `charAt(0)` で最初の文字を取得
- `toUpperCase()` で大文字に変換
- `slice(1)` で残りの文字列を取得
- `+` で連結して結合

これらの文字列メソッドは、パスカルケース変換器を作成する際に役立ちます。
