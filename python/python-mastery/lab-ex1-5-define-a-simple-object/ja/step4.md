# 複数の株式オブジェクトを扱う

オブジェクト指向プログラミングにおいて、クラスはブループリントのようなもので、そのクラスのインスタンスはそのブループリントに基づいて作成される実際のオブジェクトです。私たちの `Stock` クラスは株式を表すためのブループリントです。この `Stock` クラスの複数のインスタンスを作成して、異なる株式を表すことができます。各インスタンスは、株式名、株数、株価などの独自の属性セットを持ちます。

1. Python の対話セッションがまだ実行されている状態で、もう 1 つの `Stock` オブジェクトを作成します。今回は IBM を表すオブジェクトを作成します。`Stock` クラスのインスタンスを作成するには、クラス名を関数のように呼び出し、必要な引数を渡します。ここでの引数は、株式名、株数、株価です。

```python
t = Stock('IBM', 50, 91.5)
```

このコード行では、IBM を表す新しい `Stock` オブジェクト `t` を作成しています。このオブジェクトは 50 株を持ち、1 株あたりの価格は 91.5 ドルです。

2. 次に、この新しい株式のコストを計算します。`Stock` クラスには `cost()` というメソッドがあり、株数に株価を掛けることで株式の総コストを計算します。

```python
t.cost()
```

このコードを実行すると、Python は `t` オブジェクトの `cost()` メソッドを呼び出し、総コストを返します。

出力：

```
4575.0
```

3. Python の文字列フォーマットを使用して、株式情報を見やすく整理して表示することができます。文字列フォーマットを使うと、異なる型のデータを文字列内でどのように表示するかを指定できます。

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

このコードでは、Python の古いスタイルの文字列フォーマットを使用しています。`%` 演算子は、文字列をテンプレートとして、値を置き換えるために使用されます。文字列テンプレート `'%10s %10d %10.2f'` は、株式名、株数、株価がどのようにフォーマットされるかを定義しています。

出力：

```
      GOOG        100     490.10
```

このフォーマットされた文字列は次のように動作します。

- `%10s` は、10 文字幅のフィールドに文字列を右詰めでフォーマットします。つまり、株式名は 10 文字幅のスペースに配置され、そのスペース内で右詰めになります。
- `%10d` は、10 文字幅のフィールドに整数をフォーマットします。したがって、株数は 10 文字幅のスペースに配置されます。
- `%10.2f` は、10 文字幅のフィールドに小数点以下 2 桁の浮動小数点数をフォーマットします。株価は小数点以下 2 桁で表示され、10 文字幅のスペースに配置されます。

4. では、同じ方法で IBM の株式情報をフォーマットしましょう。文字列フォーマットのコードでオブジェクト名を `s` から `t` に置き換えるだけです。

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

出力：

```
       IBM         50      91.50
```

5. 現代の Python では、f - 文字列も使用してフォーマットすることができます。f - 文字列は読みやすく、使いやすいです。f - 文字列を使って両方の株式のコストを比較してみましょう。

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

この f - 文字列では、中括弧 `{}` の中に式を直接埋め込んでいます。Python はこれらの式を評価し、結果を文字列に挿入します。

出力：

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. 実験が終了したら、Python の対話モードを終了しましょう。`exit()` 関数を使用することでこれを行うことができます。

```python
exit()
```

各 `Stock` オブジェクトは独自の属性セットを保持しており、これはオブジェクト指向プログラミングにおけるクラスインスタンスの動作を示しています。これにより、同じメソッドを共有しながら、それぞれ異なる値を持つ複数の株式オブジェクトを作成することができます。
