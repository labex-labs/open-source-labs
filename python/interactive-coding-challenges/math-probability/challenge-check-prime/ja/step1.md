# 素数をチェックする

## 問題

整数を入力として受け取り、その数が素数であればTrueを返し、そうでなければFalseを返すPython関数を書きます。入力が整数でないか、2未満の場合、関数は例外を発生させる必要があります。

ある数が1とそれ自身のみで割り切れる場合、その数は素数と見なされます。たとえば、2、3、5、7、11、13、17、19、23、29、31、37、41、43、47、53、59、61、67、71、73、79、83、89、97が最初の25個の素数です。

## 要件

プログラムは以下の要件を満たす必要があります。

- 関数は整数を入力として受け取る必要があります。
- 入力が整数でないか、2未満の場合、関数は例外を発生させる必要があります。
- 入力が素数であれば関数はTrueを返し、そうでなければFalseを返す必要があります。
- プログラムは1を素数としては考慮しない必要があります。

## 例の使用法

- `check_prime(None)` -> `例外`
- `check_prime('hello')` -> `例外`
- `check_prime(1)` -> `False`
- `check_prime(7)` -> `True`
