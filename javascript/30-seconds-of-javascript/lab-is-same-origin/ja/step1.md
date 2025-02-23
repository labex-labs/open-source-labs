# 2つのURLが同じオリジンにあるかどうかを確認する

2つのURLが同じオリジンにあるかどうかを確認するには：

1. ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。

2. `URL.protocol` と `URL.host` を使用して、両方のURLが同じプロトコルとホストを持っているかどうかを確認します。

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. 比較したいURLで2つのURLオブジェクトを作成します。

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. 2つのURLオブジェクトを引数として `isSameOrigin` 関数を呼び出して、ブール値の出力を取得します。

```js
isSameOrigin(origin, destination); // true
```

5. 他のURLで関数をテストして、同じオリジンにあるかどうかを確認することもできます。

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
