# ISO 日付形式と JavaScript の Date オブジェクトの理解

コーディングを始める前に、ISO 8601 日付形式とは何か、および JavaScript が日付をどのように扱うかを理解しましょう。

## ISO 8601 日付形式

ISO 8601 形式は、日付と時刻を表す国際標準です。簡略拡張 ISO 形式は次のようになります。

```
YYYY-MM-DDTHH:mm:ss.sssZ
```

ここで:

- `YYYY` は年を表します (4 桁)
- `MM` は月を表します (2 桁)
- `DD` は日を表します (2 桁)
- `T` は日付と時刻を区切るリテラル文字です
- `HH` は時を表します (2 桁)
- `mm` は分を表します (2 桁)
- `ss` は秒を表します (2 桁)
- `sss` はミリ秒を表します (3 桁)
- `Z` は UTC タイムゾーン (ズールー時間) を示します

たとえば、`2023-05-12T14:30:15.123Z` は 2023 年 5 月 12 日、UTC 時間の午後 2 時 30 分 15.123 秒を表します。

## JavaScript の Date オブジェクト

JavaScript は、日付と時刻を扱うための組み込みの `Date` オブジェクトを提供しています。新しい `Date` オブジェクトを作成するときに、ISO 形式の文字列を渡すことができます。

```javascript
const date = new Date("2023-05-12T14:30:15.123Z");
```

ターミナルを開いて、Date オブジェクトの操作を練習しましょう。

1. WebIDE の上部にあるターミナルメニューをクリックして、ターミナルを開きます。
2. `node` と入力し、Enter キーを押して Node.js の対話型シェルを起動します。
3. 現在の時刻の新しい Date オブジェクトを作成します。

```javascript
const now = new Date();
console.log(now);
```

![node-prompt](../assets/screenshot-20250306-odDaT5Rp@2x.png)

4. この Date オブジェクトを ISO 文字列に変換します。

```javascript
const isoString = now.toISOString();
console.log(isoString);
```

次のような出力が表示されるはずです。

```
2023-05-12T14:30:15.123Z
```

5. ISO 文字列から Date オブジェクトを作成します。

```javascript
const dateFromIso = new Date("2023-05-12T14:30:15.123Z");
console.log(dateFromIso);
```

![node-prompt](../assets/screenshot-20250306-dbkCLkf7@2x.png)

これは、JavaScript が ISO 形式の文字列から Date オブジェクトを解析して作成できることを示しています。
