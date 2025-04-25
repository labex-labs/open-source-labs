# Python における属性アクセスの理解

Python では、オブジェクトは基本的な概念です。オブジェクトは属性にデータを格納することができ、属性は値を格納する名前付きのコンテナのようなものです。属性はオブジェクトに属する変数と考えることができます。これらの属性にアクセスする方法はいくつかあります。最も簡単で一般的に使われる方法はドット (`.`) 表記です。ただし、Python には属性を操作する際により柔軟性を与える特定の関数も用意されています。

## ドット表記

まず、`Stock` オブジェクトを作成し、ドット表記を使ってその属性を操作する方法を見てみましょう。ドット表記は、オブジェクトの属性にアクセスして変更するためのシンプルで直感的な方法です。

まず、新しいターミナルを開き、Python の対話型シェルを起動します。ここでは、Python コードを 1 行ずつ書いて実行することができます。

```python
# Open a new terminal and run Python interactive shell
python3

# Import the Stock class from the stock module
from stock import Stock

# Create a Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(s.name)    # Output: 'GOOG'

# Set an attribute
s.shares = 50
print(s.shares)  # Output: 50

# Delete an attribute
del s.shares
# If we try to access s.shares now, we'll get an AttributeError
```

上記のコードでは、まず `stock` モジュールから `Stock` クラスをインポートします。次に、`Stock` クラスのインスタンス `s` を作成します。`name` 属性の値を取得するには、`s.name` を使用します。`shares` 属性の値を変更するには、`s.shares` に新しい値を代入するだけです。属性を削除する場合は、`del` キーワードの後に属性名を指定します。

## 属性アクセス関数

Python には、属性の操作に非常に便利な 4 つの組み込み関数が用意されています。これらの関数は、属性を操作する際に、特に動的に属性を扱う必要がある場合に、より多くの制御を与えます。

1. `getattr()` - この関数は、属性の値を取得するために使用されます。
2. `setattr()` - この関数を使用すると、属性の値を設定することができます。
3. `delattr()` - この関数を使用して属性を削除することができます。
4. `hasattr()` - この関数は、オブジェクトに属性が存在するかどうかをチェックします。

これらの関数の使い方を見てみましょう。

```python
# Create a new Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(getattr(s, 'name'))       # Output: 'GOOG'

# Set an attribute
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Check if an attribute exists
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Delete an attribute
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

これらの関数は、属性を動的に扱う必要がある場合に特に便利です。ハードコードされた属性名を使用する代わりに、変数名を使用することができます。たとえば、属性名を格納する変数がある場合、その変数をこれらの関数に渡して、対応する属性に対して操作を実行することができます。これにより、特に異なるオブジェクトや属性をより動的に扱う場合に、コードにより多くの柔軟性が与えられます。
