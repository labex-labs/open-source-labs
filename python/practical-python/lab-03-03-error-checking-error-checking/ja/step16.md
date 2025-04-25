# 演習 3.10：エラーの抑制

`parse_csv()` 関数を修正して、ユーザーが明示的に希望する場合には、解析エラーメッセージを抑制できるようにします。たとえば：

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```

エラーハンドリングは、ほとんどのプログラムで正しく行うのが最も困難なことの 1 つです。一般的なルールとして、エラーを黙って無視してはなりません。代わりに、問題を報告し、ユーザーがそう選択した場合にエラーメッセージを抑制するオプションを与える方が良いです。
