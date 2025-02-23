# 整数の午前・午後接尾辞を取得する方法

コーディングを始めるには、ターミナル/SSH を開き、`node` と入力します。

ここに、整数を午前・午後接尾辞付きの 12 時間形式の文字列に変換する関数があります。

これを行うには、剰余演算子 (`%`) と条件判定を使用します。

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

この関数の使用例をいくつか示します。

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

この関数は整数を引数として受け取り、午前・午後接尾辞付きの文字列を返します。
