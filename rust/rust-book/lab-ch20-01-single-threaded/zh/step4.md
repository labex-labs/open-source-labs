# 深入了解 HTTP 请求

HTTP 是一种基于文本的协议，请求采用以下格式：

    方法 请求-URI HTTP版本 CRLF
    头部信息 CRLF
    消息体

第一行是**请求行**，包含有关客户端请求内容的信息。请求行的第一部分表示所使用的**方法**，例如`GET`或`POST`，它描述了客户端如何发出此请求。我们的客户端使用了`GET`请求，这意味着它在请求信息。

请求行的下一部分是`/_`，它表示客户端请求的**统一资源标识符**（_uniform resource identifier_，**URI**）：URI 几乎与**统一资源定位符**（_uniform resource locator_，**URL**）相同，但不完全一样。在本章中，URI 和 URL 之间的区别对我们的目的来说并不重要，但 HTTP 规范使用术语**URI**，所以在这里我们可以在心里将**URI**替换为**URL**。

最后一部分是客户端使用的 HTTP 版本，然后请求行以 CRLF 序列结束。（CRLF 代表**回车**和**换行**，这是打字机时代的术语！）CRLF 序列也可以写成`\r\n`，其中`\r`是回车，`\n`是换行。**CRLF 序列**将请求行与请求数据的其余部分分隔开。请注意，当打印 CRLF 时，我们看到的是新行开始，而不是`\r\n`。

查看我们目前运行程序收到的请求行数据，我们可以看到`GET`是方法，`/_`是请求 URI，`HTTP/1.1`是版本。

在请求行之后，从`Host:`开始的其余行是头部信息。`GET`请求没有消息体。

尝试从不同的浏览器发出请求，或者请求不同的地址，例如`127.0.0.1:7878/test`，看看请求数据如何变化。

现在我们知道了浏览器在请求什么，让我们返回一些数据！
