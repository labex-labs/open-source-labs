# 로깅 설정

로깅 동작은 별도로 구성됩니다.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # 로그 출력 파일
        level     = logging.INFO,   # 출력 레벨
    )
```

일반적으로, 이것은 프로그램 시작 시 한 번 수행되는 설정입니다. 설정은 로깅 호출을 하는 코드와 분리되어 있습니다.
