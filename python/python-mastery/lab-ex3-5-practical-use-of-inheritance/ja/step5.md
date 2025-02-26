# 選択を簡単にする

継承を使用する際の 1 つの問題は、使用する異なるクラスを選ぶ際の追加の複雑さです（たとえば、名前を覚えること、正しい `import` 文を使用することなど）。ファクトリ関数を使うことでこれを簡素化できます。`tableformat.py` ファイルに、ユーザーが `'text'`、`'csv'`、または `'html'` などの形式を指定することで、より簡単にフォーマッタを作成できるようにする `create_formatter()` 関数を追加します。たとえば：

```python
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('html')
>>> print_table(portfolio, ['name','shares','price'], formatter)
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
>>>
```

**考察**

この演習での `TableFormatter` クラスは、「抽象基底クラス」として知られるものの例です。これは直接使用することを想定されているものではありません。代わりに、これはプログラムコンポーネント（この場合、さまざまな出力形式）の一種のインターフェイス仕様として機能しています。基本的に、表を生成するコードは、ユーザーが適切な実装を提供することを期待して、抽象基底クラスに対してプログラムされます。必要なすべてのメソッドが実装されていれば、すべてがうまく「機能するはず」です（念のため）。
