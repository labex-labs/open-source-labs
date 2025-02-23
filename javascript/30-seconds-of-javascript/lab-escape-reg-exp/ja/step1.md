# JavaScript で正規表現をエスケープする方法

JavaScript の正規表現で使用するために文字列をエスケープするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 特殊文字をエスケープするには、`String.prototype.replace()` を使用します。
3. 次のコード スニペットをコピーして貼り付けます。

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4. `escapeRegExp()` 関数を使用して、文字列内の特殊文字をエスケープします。

以下は例です。

```js
escapeRegExp("(test)"); // \\(test\\)
```

これらの手順により、JavaScript の正規表現で任意の特殊文字を簡単にエスケープできるようになりました。
