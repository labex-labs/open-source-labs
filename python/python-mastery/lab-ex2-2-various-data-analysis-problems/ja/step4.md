# シカゴ交通局のデータを用いたデータ分析チャレンジ

これまでに、さまざまなPythonのデータ構造と`collections`モジュールを使った練習を行ってきました。それでは、これらのスキルを実世界のデータ分析タスクに活かしてみましょう。この実験では、シカゴ交通局（CTA）のバス乗車率データを分析します。この実践的なアプリケーションを通じて、Pythonを使って実世界のデータセットから有意義な情報を抽出する方法を理解することができます。

## データの理解

まず、扱う交通データを見てみましょう。Pythonターミナルで、データをロードして基本構造を理解するためのコードを実行します。

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

`import readrides`文は、CSVファイルからデータを読み取る関数を持つカスタムモジュールをインポートします。`readrides.read_rides_as_dicts`関数は、指定されたCSVファイルからデータを読み取り、各行を辞書に変換します。`len(rows)`はデータセット内のレコードの総数を返します。`pprint.pprint(rows[0])`を使って最初のレコードを印刷することで、各レコードの構造を明確に確認することができます。

このデータには、さまざまなバス路線の日々の乗車記録が含まれています。各レコードには以下の情報が含まれています。

- `route`：バス路線番号
- `date`："YYYY - MM - DD"形式の日付
- `daytype`：平日は"W"、土曜日は"A"、日曜日/祝日は"U"
- `rides`：その日の乗車人数

## 分析タスク

チャレンジの各質問を1つずつ解いていきましょう。

### 質問1：シカゴには何本のバス路線がありますか？

この質問に答えるには、データセット内のすべての一意の路線番号を見つける必要があります。このタスクにはセット内包表記を使用します。

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

セット内包表記は、セットを作成する簡潔な方法です。この場合、`rows`リストの各行を反復処理し、`route`値を抽出します。セットは一意の要素のみを格納するため、すべての一意の路線番号のセットが得られます。このセットの長さを印刷することで、一意のバス路線の総数がわかります。

これらの路線の一部を見ることもできます。

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

ここでは、一意の路線のセットをリストに変換し、そのリストの最初の10要素を印刷します。

### 質問2：2011年2月2日に22号バスには何人が乗車しましたか？

この質問に答えるには、与えられた路線と日付に一致する特定のレコードを見つけるためにデータをフィルタリングする必要があります。

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

まず、`target_date`と`target_route`変数を定義します。次に、`rows`リストの各行を反復処理します。各行について、`route`と`date`がターゲット値と一致するかどうかを確認します。一致するレコードが見つかったら、乗車人数を印刷し、目的のレコードを見つけたのでループを抜けます。

`target_date`と`target_route`変数を変更することで、任意の日付の任意の路線を確認するようにこのコードを変更することができます。

### 質問3：各バス路線の総乗車人数はいくらですか？

各路線の総乗車人数を計算するために`Counter`を使用しましょう。`Counter`は`collections`モジュールからの辞書のサブクラスで、ハッシュ可能なオブジェクトをカウントするために使用されます。

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

まず、`collections`モジュールから`Counter`クラスをインポートします。次に、`total_rides_by_route`という空のカウンターを初期化します。`rows`リストの各行を反復処理する際に、各路線の乗車人数をカウンターに追加します。最後に、`most_common(5)`メソッドを使って、総乗車人数が最も多い上位5つの路線を取得し、結果を印刷します。

### 質問4：2001年から2011年までの10年間で乗車率の増加が最も大きかった5本のバス路線はどれですか？

これはより複雑なタスクです。各路線について、2001年の乗車率と2011年の乗車率を比較する必要があります。

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

まず、2001年と2011年の各路線の総乗車人数をそれぞれ格納するために、2つの`Counter`オブジェクト`rides_2001`と`rides_2011`を作成します。`rows`リストの各行を反復処理する際に、日付が'2001 -'または'2011 -'で始まるかどうかを確認し、適切なカウンターに乗車人数を追加します。

次に、各路線の乗車率の増加を格納するための空の辞書`increases`を作成します。一意の路線を反復処理し、各路線について2011年の乗車人数から2001年の乗車人数を引いて増加量を計算します。

増加量が最も大きい上位5つの路線を見つけるために、`heapq.nlargest`関数を使用します。この関数は、返す要素の数（この場合は5）、反復可能オブジェクト（`increases.items()`）、および要素を比較する方法を指定するキー関数（`lambda x: x[1]`）を受け取ります。

最後に、路線番号、乗車率の増加量、2001年と2011年の乗車人数を表示して結果を印刷します。

この分析により、10年間で乗車率の最も大きな増加を経験したバス路線が特定され、これは人口パターンの変化、サービスの改善、またはその他の興味深い傾向を示す可能性があります。

これらの分析を多くの方法で拡張することができます。たとえば、以下のことを行いたいかもしれません。

- 曜日ごとの乗車率パターンを分析する
- 乗車率が減少している路線を見つける
- 乗車率の季節変動を比較する

この実験で学んだ技術は、このようなデータ探索と分析のための堅固な基礎を提供します。
