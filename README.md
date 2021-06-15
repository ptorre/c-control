# c-control
### Remote control for chrome, chromium or embedded chromium using websockets.

Start chrome, or chromium with the following options:
```
--remote-debugging-address=0.0.0.0 --remote-debugging-port=9222
```

Start embeded Qt WebEngine with these variables set in the environment:
```
QTWEBENGINE_DISABLE_SANDBOX=1
QTWEBENGINE_REMOTE_DEBUGGING=0.0.0.0:9222
```

export CHROME_WS=$(http http://192.168.1.128:9222/json | jq .[0].webSocketDebuggerUrl| sed -e 's/"//g')

