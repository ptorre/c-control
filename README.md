# c-control
Remote control for embedded chromium using websockets

Start chrome, or chromium with --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222

Start embeded Qt WebEngine with these variables set in the environment:
QTWEBENGINE_DISABLE_SANDBOX=1
QTWEBENGINE_REMOTE_DEBUGGING=0.0.0.0:9222


