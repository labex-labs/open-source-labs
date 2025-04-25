# Python におけるバウンドメソッドの理解

Python では、メソッドは呼び出すことができる特殊なタイプの属性です。オブジェクトを通じてメソッドにアクセスすると、「バウンドメソッド」と呼ばれるものを取得します。バウンドメソッドは本質的に、特定のオブジェクトに紐付けられたメソッドです。これは、オブジェクトのデータにアクセスし、それを操作することができることを意味します。

## メソッドを属性としてアクセスする

`Stock` クラスを使って、バウンドメソッドを探索してみましょう。まず、メソッドをオブジェクトの属性としてアクセスする方法を見てみます。

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

上記のコードでは、まず `Stock` クラスをインポートし、そのインスタンスを作成します。次に、`s` オブジェクトの `cost` メソッドを実際に呼び出すことなくアクセスします。これにより、バウンドメソッドが得られます。このバウンドメソッドを呼び出すと、オブジェクトのデータに基づいてコストが計算されます。また、オブジェクトに対してメソッドを直接 1 ステップで呼び出すこともできます。

## getattr() を使ったメソッドのアクセス

メソッドにアクセスする別の方法は、`getattr()` 関数を使用することです。この関数を使うと、名前でオブジェクトの属性を取得できます。

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

ここでは、`getattr()` を使って `s` オブジェクトから `cost` メソッドを取得します。前と同じように、バウンドメソッドを呼び出して結果を得ることができます。また、メソッドの取得と呼び出しを 1 行で行うこともできます。

## バウンドメソッドとそのオブジェクト

バウンドメソッドは、アクセス元のオブジェクトへの参照を常に保持します。これは、メソッドを変数に格納しても、それがどのオブジェクトに属しているかを知り、オブジェクトのデータにアクセスできることを意味します。

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

この例では、`cost` メソッドを変数 `c` に格納します。`c()` を呼び出すと、オブジェクトの現在のデータに基づいてコストが計算されます。次に、`s` オブジェクトの `shares` 属性を変更します。再度 `c()` を呼び出すと、更新されたデータを使って新しいコストが計算されます。

## バウンドメソッドの内部を探索する

バウンドメソッドには、それに関するより多くの情報を提供する 2 つの重要な属性があります。

- `__self__`: この属性は、メソッドが紐付けられているオブジェクトを参照します。
- `__func__`: この属性は、メソッドを表す実際の関数オブジェクトです。

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

ここでは、バウンドメソッド `c` の `__self__` と `__func__` 属性にアクセスします。`__self__` が `s` オブジェクトで、`__func__` が `cost` 関数であることがわかります。オブジェクトを引数として渡して関数を手動で呼び出すこともでき、これはバウンドメソッドを直接呼び出すのと同じ結果を得ます。

## 引数を取るメソッドの例

引数を取るメソッド（例えば `sell()` メソッド）でバウンドメソッドがどのように動作するか見てみましょう。

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

この例では、`sell` メソッドをバウンドメソッドとして取得します。引数を指定して呼び出すと、`s` オブジェクトの `shares` 属性が更新されます。`__func__` と `__self__` 属性を使ってメソッドを手動で呼び出し、引数も渡すこともできます。

バウンドメソッドを理解することは、Python のオブジェクトシステムが内部でどのように動作するかを理解するのに役立ちます。これは、デバッグ、メタプログラミング、高度なプログラミングパターンの作成に役立ちます。
