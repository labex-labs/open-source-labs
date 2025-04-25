# JavaScript でタブを半角スペースに変換する方法

コーディング時にタブ文字を半角スペースに変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために`node`と入力します。
2. 正規表現と`String.prototype.repeat()`を使って`String.prototype.replace()`メソッドを使い、各タブ文字を必要な数の半角スペースに置き換えます。
3. 以下のコードスニペットは、`expandTabs`関数を使ってタブを半角スペースに置き換える方法を示しています。

```js
const expandTabs = (str, count) => str.replace(/\t/g, " ".repeat(count));

expandTabs("\t\tlorem", 3); // '      lorem'
```

上記の例では、`expandTabs`関数は 2 つの引数をとります。タブを含む文字列`str`と、各タブ文字を置き換える半角スペースの数を表す数値`count`です。この関数は、正規表現 (`/\t/g`) を使った`String.prototype.replace()`メソッドを使って、入力文字列内のすべてのタブ文字を見つけ、`String.prototype.repeat()`メソッドを使って必要な数の半角スペースに置き換えます。
