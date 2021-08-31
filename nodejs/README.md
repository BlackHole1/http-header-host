### test curl command

Node.js Source code: [github/nodejs/node/src/node_http_parser.cc#L818-L828](https://github.com/nodejs/node/blob/9eff8191f244bd321a43355dcac8c712afc382bd/src/node_http_parser.cc#L818-L828)

#### not has Host

```shell
curl 'http://127.0.0.1:8082' -H 'User-Agent:' -H 'Accept:' -H 'Host:'
```

result:

```
{"status":true,"headers":{}}
```

#### has Host

```shell
curl 'http://127.0.0.1:8082' -H 'User-Agent:' -H 'Accept:'
```

result

```
{"status":true,"headers":{"host":"127.0.0.1:8082"}}
```

