# 단일 스레드 웹 서버 구축

단일 스레드 웹 서버를 작동시키는 것부터 시작합니다. 시작하기 전에 웹 서버 구축에 관련된 프로토콜에 대한 간략한 개요를 살펴보겠습니다. 이러한 프로토콜의 세부 사항은 이 책의 범위를 벗어나지만, 간략한 개요를 통해 필요한 정보를 얻을 수 있습니다.

웹 서버와 관련된 두 가지 주요 프로토콜은 _Hypertext Transfer Protocol_ (HTTP, 하이퍼텍스트 전송 프로토콜) 와 _Transmission Control Protocol_ (TCP, 전송 제어 프로토콜) 입니다. 두 프로토콜 모두 _request-response_ (요청 - 응답) 프로토콜로, _client_ (클라이언트) 가 요청을 시작하고 _server_ (서버) 가 요청을 수신하여 클라이언트에게 응답을 제공합니다. 이러한 요청과 응답의 내용은 프로토콜에 의해 정의됩니다.

TCP 는 정보가 한 서버에서 다른 서버로 어떻게 전달되는지에 대한 세부 사항을 설명하는 하위 레벨 프로토콜이지만, 해당 정보가 무엇인지 지정하지는 않습니다. HTTP 는 TCP 를 기반으로 구축되어 요청 및 응답의 내용을 정의합니다. 기술적으로는 다른 프로토콜과 함께 HTTP 를 사용하는 것이 가능하지만, 대부분의 경우 HTTP 는 TCP 를 통해 데이터를 전송합니다. 우리는 TCP 및 HTTP 요청과 응답의 원시 바이트 (raw bytes) 로 작업할 것입니다.
