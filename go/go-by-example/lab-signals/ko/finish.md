# 요약

Signals 랩은 Go 프로그램에서 채널을 사용하여 Unix 시그널을 처리하는 방법을 보여줍니다. `os.Signal` 알림을 수신하기 위해 버퍼링된 채널을 생성하고 `signal.Notify`를 사용하여 지정된 시그널의 알림을 수신하도록 채널을 등록함으로써, 예상된 시그널이 수신될 때 시그널을 정상적으로 처리하고 프로그램을 종료할 수 있습니다.
