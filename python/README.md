### test curl command

Python Source code: [github/python/cpython/Lib/http/client.py#L205-L221](https://github.com/python/cpython/blob/47895e31b6f626bc6ce47d175fe9d43c1098909d/Lib/http/client.py#L205-L221)

#### not has Host

```shell
curl 'http://127.0.0.1:8084' -H 'User-Agent:' -H 'Accept:' -H 'Host:'
```

result:

```
{"status": true, "headers": {}}
```

#### has Host

```shell
curl 'http://127.0.0.1:8084' -H 'User-Agent:' -H 'Accept:'
```

result

```
{"status": true, "headers": {"Host": "127.0.0.1:8084"}}
```

