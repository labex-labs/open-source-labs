# より高度な Python プログラムを作成する

Python の基本をマスターしたので、次のステップとして、より高度な Python プログラムを作成しましょう。このプログラムは ASCII アートパターンを生成します。ASCII アートは、テキスト文字で構成されるシンプルで視覚的に面白いデザインです。このプログラムに取り組むことで、モジュールのインポート、関数の定義、コマンドライン引数の処理など、いくつかの重要な Python の概念を学び、適用することができます。

## ASCII アートプログラムを作成する

1. まず、WebIDE で `art.py` ファイルを開きます。このファイルはセットアップ時に作成されました。`/home/labex/project` ディレクトリにあります。このファイルを開くことが、ASCII アートプログラムを書くための始点となります。

2. ファイルを開くと、既存の内容があるかもしれません。これからゼロから自分たちのコードを書くので、その内容をクリアする必要があります。ファイル内の既存の内容をすべて削除してから、次のコードを `art.py` ファイルにコピーします。このコードが、私たちの ASCII アートジェネレータの核心部分です。

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. コードをファイルにコピーしたら、作業内容を保存することが重要です。キーボードで Ctrl + S を押すか、メニューから「ファイル」>「保存」を選択して保存できます。ファイルを保存することで、コードが保存され、実行できる状態になります。

## コードの理解

このプログラムが何をするのか、もう少し詳しく見てみましょう。コードを理解することは、将来的にコードを修正したり拡張したりするために重要です。

- **インポート文**: `import sys` と `import random` の行は、Python の組み込みモジュールを取り込むために使用されます。`sys` モジュールは、Python インタプリタが使用または維持するいくつかの変数や、インタプリタと強く相互作用する関数にアクセスするためのものです。`random` モジュールは、乱数を生成するために使用され、これを使ってランダムな ASCII アートパターンを作成します。
- **文字セット**: `chars = '\|/'` の行は、ASCII アートを作成するために使用する文字セットを定義します。これらの文字は、パターンを形成するためにランダムに選択されます。
- **`draw()` 関数**: この関数は、ASCII アートパターンを作成する役割を担っています。`rows` と `columns` という 2 つの引数を取り、これらはパターンの寸法を指定します。関数の内部では、ループを使って `chars` セットから文字をランダムに選択し、パターンの各行を作成します。
- **メインブロック**: `if __name__ == '__main__':` ブロックは、Python の特別な構造です。このブロック内のコードは、`art.py` ファイルが直接実行されたときにのみ実行されます。このファイルが別の Python ファイルにインポートされた場合は、このコードは実行されません。
- **引数の処理**: `sys.argv` 変数には、プログラムに渡されたコマンドライン引数が含まれています。正確に 3 つの引数（スクリプト自体の名前と、行数と列数を表す 2 つの数値）が提供されているかを確認します。これにより、ユーザーが正しい入力を提供することを保証します。
- **エラー処理**: `try/except` ブロックは、発生する可能性のあるエラーを捕捉するために使用されます。ユーザーが無効な入力（行数や列数に整数でない値）を提供した場合、`try` ブロックで `ValueError` が発生し、`except` ブロックでエラーメッセージが表示され、プログラムが終了します。

## プログラムを実行する

1. プログラムを実行するには、まず WebIDE でターミナルを開く必要があります。ターミナルで Python スクリプトを実行するためのコマンドを入力します。

2. ターミナルを開いたら、プロジェクトディレクトリに移動する必要があります。ここに `art.py` ファイルがあります。ターミナルで次のコマンドを使用します。

   ```bash
   cd ~/project
   ```

   このコマンドは、現在の作業ディレクトリをプロジェクトディレクトリに変更します。

3. 正しいディレクトリに移動したら、プログラムを実行できます。次のコマンドを使用します。

   ```bash
   python3 art.py 5 10
   ```

   このコマンドは、Python に `art.py` スクリプトを 5 行 10 列で実行するように指示します。このコマンドを実行すると、ターミナルに 5×10 の文字パターンが表示されます。出力は次のようになります。

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   実際のパターンはランダムなので、ここに示した例とは異なります。

4. コマンドの引数を変更することで、異なる寸法のパターンを試すことができます。たとえば、次のコマンドを試してみましょう。

   ```bash
   python3 art.py 8 15
   ```

   これにより、8 行 15 列の大きなパターンが生成されます。

5. エラー処理の動作を確認するには、無効な引数を提供してみましょう。次のコマンドを実行します。

   ```bash
   python3 art.py
   ```

   次のようなエラーメッセージが表示されるはずです。

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## コードを試す

文字セットを変更することで、ASCII アートパターンをより面白いものにすることができます。以下はその方法です。

1. エディタで再度 `art.py` ファイルを開きます。ここでコードを変更します。

2. コード内の `chars` 変数を見つけます。異なる文字を使用するように変更します。たとえば、次のコードを使用できます。

   ```python
   chars = '*#@+.'
   ```

   これにより、ASCII アートを作成するために使用する文字セットが変更されます。

3. 変更を加えた後、Ctrl + S または「ファイル」>「保存」を使用してファイルを再度保存します。その後、次のコマンドでプログラムを実行します。

   ```bash
   python3 art.py 5 10
   ```

   これで、新しい文字を使用した異なるパターンが表示されます。

この演習では、いくつかの重要な Python の概念が示されています。

- モジュールのインポート: Python の組み込みモジュールから追加の機能を取り込む方法。
- 関数の定義: コードを整理するために関数を定義し、使用する方法。
- コマンドライン引数の処理: コマンドラインからユーザー入力を受け取り、処理する方法。
- try/except によるエラー処理: プログラムでエラーを適切に処理する方法。
- 文字列操作: ASCII アートパターンを形成するために文字列を作成し、操作する方法。
- 乱数生成: ユニークなパターンを作成するために乱数を生成する方法。
- リスト内包表記: Python でリストを簡潔に作成する方法で、`draw()` 関数で使用されています。
