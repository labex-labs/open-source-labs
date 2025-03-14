# リストのメモリ割り当ての理解

Python では、リストは非常に便利なデータ構造であり、特に要素を追加する必要がある場合に便利です。Python のリストは、要素の追加操作に効率的に設計されています。必要なメモリ量を正確に割り当てる代わりに、Python は将来の追加を見越して余分なメモリを割り当てます。この戦略により、リストが拡張される際に必要なメモリの再割り当て回数が最小限に抑えられます。

`sys.getsizeof()` 関数を使用して、この概念をもっとよく理解しましょう。この関数は、オブジェクトのサイズをバイト単位で返し、リストが異なる段階でどれだけのメモリを使用しているかを確認するのに役立ちます。

1. まず、ターミナルで Python の対話型シェルを開く必要があります。これは、Python コードをすぐに実行できるプレイグラウンドのようなものです。開くには、ターミナルに以下のコマンドを入力して Enter キーを押します。

```bash
python3
```

2. Python の対話型シェルに入ったら、`sys` モジュールをインポートする必要があります。Python のモジュールは、便利な関数が入ったツールボックスのようなものです。`sys` モジュールには、必要な `getsizeof()` 関数があります。モジュールをインポートした後、`items` という名前の空のリストを作成します。以下はそのコードです。

```python
import sys
items = []
```

3. では、空のリストの初期サイズを確認しましょう。`sys.getsizeof()` 関数を `items` リストを引数として使用します。Python の対話型シェルに以下のコードを入力して Enter キーを押します。

```python
sys.getsizeof(items)
```

`64` バイトのような値が表示されるはずです。この値は、空のリストのオーバーヘッドを表しています。オーバーヘッドは、リストに要素がない場合でも、Python がリストを管理するために使用する基本的なメモリ量です。

4. 次に、リストに要素を 1 つずつ追加して、メモリ割り当てがどのように変化するかを観察します。`append()` メソッドを使用して要素をリストに追加し、再度サイズを確認します。以下はそのコードです。

```python
items.append(1)
sys.getsizeof(items)
```

`96` バイト程度の大きな値が表示されるはずです。このサイズの増加は、Python が新しい要素を収容するためにより多くのメモリを割り当てたことを示しています。

5. リストにさらに要素を追加し、各追加後にサイズを確認しましょう。以下はそのコードです。

```python
items.append(2)
sys.getsizeof(items)  # サイズは同じまま

items.append(3)
sys.getsizeof(items)  # サイズはまだ変わらない

items.append(4)
sys.getsizeof(items)  # サイズはまだ変わらない

items.append(5)
sys.getsizeof(items)  # サイズが大きく増加する
```

追加操作のたびにサイズが増加するわけではないことに気づくでしょう。代わりに、定期的にサイズが増加します。これは、Python が各新しい要素に個別にメモリを割り当てるのではなく、チャンク単位でメモリを割り当てていることを示しています。

この動作は設計上のものです。Python は、リストが拡張される際に頻繁な再割り当てを避けるために、最初に必要以上のメモリを割り当てます。リストが現在の容量を超えるたびに、Python はより大きなメモリチャンクを割り当てます。

リストはオブジェクト自体ではなく、オブジェクトへの参照を格納することを忘れないでください。64 ビットシステムでは、各参照には通常 8 バイトのメモリが必要です。これは、リストが異なるタイプのオブジェクトを含む場合に、リストが実際に使用するメモリ量に影響を与えるため、理解するのが重要です。
