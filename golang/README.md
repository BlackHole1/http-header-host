### test curl command

Golang Source code: [github/golang/go/src/net/http/server.go#L983-L985](https://github.com/golang/go/blob/d77f4c0c5c966c37960cd691656fba184ae770ff/src/net/http/server.go#L983-L985)

#### not has Host

```shell
curl 'http://127.0.0.1:8083' -H 'User-Agent:' -H 'Accept:' -H 'Host:'
```

result:

```
400 Bad Request: missing required Host header
```

#### has Host

```shell
curl 'http://127.0.0.1:8083' -H 'User-Agent:' -H 'Accept:'
```

result

```
{true map[]}
```

