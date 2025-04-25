# ターミナル/SSH でコーディングを始める方法

ターミナル/SSH でコーディングを始めるには、単に `node` と入力します。

# 複数行の文字列を行の配列に分割する

複数行の文字列を行の配列に分割するには：

- `String.prototype.split()` と正規表現を使って、改行をマッチさせて配列を作成します。
- 正規表現 `/\r?\n/` は `\r` と `\n` の両方の改行をマッチします。
- これにより、行の配列が返されます。

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a','multiline','string.', '']
```
