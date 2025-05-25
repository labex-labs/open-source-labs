# 애플리케이션 구조 (Application Structure)

코드 구성과 파일 구조는 애플리케이션의 유지 관리 가능성에 핵심입니다.

Python 에는 "모두를 위한 하나의 해결책 (one-size fits all)" 접근 방식은 없습니다. 하지만, 많은 문제에 적용되는 구조는 다음과 같습니다.

```code
porty-app/
  README.txt
  script.py         # 스크립트 (SCRIPT)
  porty/
    # 라이브러리 코드 (LIBRARY CODE)
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

최상위 레벨의 `porty-app`은 문서, 최상위 레벨 스크립트, 예제 등을 위한 컨테이너입니다.

다시 말하지만, 최상위 레벨 스크립트 (있는 경우) 는 코드 패키지 외부, 한 단계 위에 존재해야 합니다.

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

이 시점에서, 여러 프로그램이 있는 디렉토리가 있습니다:

    pcost.py          # 포트폴리오 비용 계산 (computes portfolio cost)
    report.py         # 보고서 생성 (Makes a report)
    ticker.py         # 실시간 주식 시세 표시 (Produce a real-time stock ticker)

다양한 기능을 가진 여러 지원 모듈이 있습니다:

    stock.py          # 주식 클래스 (Stock class)
    portfolio.py      # 포트폴리오 클래스 (Portfolio class)
    fileparse.py      # CSV 파싱 (CSV parsing)
    tableformat.py    # 서식 있는 테이블 (Formatted tables)
    follow.py         # 로그 파일 추적 (Follow a log file)
    typedproperty.py  # 타입 지정 클래스 속성 (Typed class properties)

이 연습에서는 코드를 정리하고 공통 패키지에 넣을 것입니다.
