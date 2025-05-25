# 연습 문제 8.3: 프로그램에 로깅 추가하기

애플리케이션에 로깅을 추가하려면, 메인 모듈에서 로깅 모듈을 초기화하는 메커니즘이 필요합니다. 이를 수행하는 한 가지 방법은 다음과 같은 설정 코드를 포함하는 것입니다.

    # 이 파일은 로깅 모듈의 기본 구성을 설정합니다.
    # 필요에 따라 로깅 출력을 조정하려면 여기에서 설정을 변경하십시오.
    import logging
    logging.basicConfig(
        filename = 'app.log',            # 로그 파일의 이름 (stderr를 사용하려면 생략)
        filemode = 'w',                  # 파일 모드 ('a'를 사용하여 추가)
        level    = logging.WARNING,      # 로깅 레벨 (DEBUG, INFO, WARNING, ERROR, 또는 CRITICAL)
    )

다시 말하지만, 이 코드를 프로그램의 시작 단계 어딘가에 넣어야 합니다. 예를 들어, `report.py` 프로그램의 어디에 이 코드를 넣을 수 있습니까?
