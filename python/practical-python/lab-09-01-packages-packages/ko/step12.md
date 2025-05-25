# 연습 9.2: 애플리케이션 디렉토리 만들기

모든 코드를 "패키지"에 넣는 것만으로는 애플리케이션에 충분하지 않은 경우가 많습니다. 때로는 지원 파일, 문서, 스크립트 및 기타 항목이 있습니다. 이러한 파일은 위에서 만든 `porty/` 디렉토리 밖에 존재해야 합니다.

`porty-app`이라는 새 디렉토리를 만듭니다. 연습 9.1 에서 만든 `porty` 디렉토리를 해당 디렉토리로 이동합니다. `portfolio.csv` 및 `prices.csv` 테스트 파일을 이 디렉토리로 복사합니다. 또한 자신에 대한 몇 가지 정보가 포함된 `README.txt` 파일을 만듭니다. 이제 코드는 다음과 같이 구성되어야 합니다:

    porty-app/
        portfolio.csv
        prices.csv
        README.txt
        porty/
            __init__.py
            fileparse.py
            follow.py
            pcost.py
            portfolio.py
            report.py
            stock.py
            tableformat.py
            ticker.py
            typedproperty.py

코드를 실행하려면 최상위 레벨의 `porty-app/` 디렉토리에서 작업하고 있는지 확인해야 합니다. 예를 들어, 터미널에서:

```python
$ cd porty-app
$ python3
>>> import porty.report
>>>
```

이전 스크립트 중 일부를 메인 프로그램으로 실행해 봅니다:

```python
$ cd porty-app
$ python3 -m porty.report portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

$
```
