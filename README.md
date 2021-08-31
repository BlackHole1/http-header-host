## http-header-host

Analyze the handling of header host in different languages

### [rfc2822 - 2.2. Header Fields](https://datatracker.ietf.org/doc/html/rfc2822#section-2.2)

There is no mention in this specification of a requirement for the `host` to exist

### [rfc7230 - 5.4 Host](https://datatracker.ietf.org/doc/html/rfc7230#section-5.4)

> When a proxy receives a request with an absolute-form of  request-target, the proxy MUST ignore the received Host header field (if any) and instead replace it with the host information of the  request-target.  A proxy that forwards such a request MUST generate a new Host field-value based on the received request-target rather than forward the received Host field-value.

> A server MUST respond with a 400 (Bad Request) status code to any HTTP/1.1 request message that lacks a Host header field and to any request message that contains more than one Host header field or a Host header field with an invalid field-value.

When there is no `Host`, we can treat it as `absolute-form`. So it shouldn't report an error either

### Result

nodejs / python is normal

golang will report an error