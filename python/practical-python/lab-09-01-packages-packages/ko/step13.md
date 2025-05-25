# 연습 9.3: 최상위 스크립트

`python -m` 명령어를 사용하는 것은 종종 약간 이상합니다. 패키지의 특이성을 처리하는 최상위 스크립트를 작성하고 싶을 수 있습니다. 위의 보고서를 생성하는 `print-report.py` 스크립트를 만듭니다:

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

이 스크립트를 최상위 `porty-app/` 디렉토리에 넣습니다. 해당 위치에서 실행할 수 있는지 확인합니다:

    $ cd porty-app
    $ python3 print-report.py portfolio.csv prices.csv txt
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

최종 코드는 이제 다음과 같은 구조를 가져야 합니다:

    porty-app/
        portfolio.csv
        prices.csv
        print-report.py
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
