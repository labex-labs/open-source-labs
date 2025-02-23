# 空白を削除する関数

文字列を空白から削除するには、次の関数を使用します。

- `String.prototype.replace()` を使って正規表現で空白文字のすべての出現を空文字列に置き換えます。

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## 正規表現の解説

- `/\s+/g` は次のように解釈されます。
  - `\s`: 任意の空白文字（スペース、タブ、改行）を一致させます
  - `+`: 直前の文字の1回以上の出現を一致させます
  - `/g`: グローバルフラグ - 文字列内のすべての出現を一致させます。最初の1つだけではなく

## 正規表現のクイックリファレンス

一般的な空白パターン:

- `\s` - 任意の空白（スペース、タブ、改行）を一致させます
- `\t` - タブ文字を一致させます
- `\n` - 改行文字を一致させます
- `\r` - 復帰文字を一致させます
- `` (スペース) - スペース文字のみを一致させます

たとえば、

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// さらに例:
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。
