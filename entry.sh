#!/bin/bash

# run OpenWebRX
cd /usr/src/app/openwebrx
git pull
chmod +x openwebrx.py
./openwebrx.py
