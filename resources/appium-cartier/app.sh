#!/bin/bash/
#echo "Connect to remote devices and start appium"


adb devices

adb connect {{device_address}}

adb push /apk_shell/app-Fir-release-4.16.020.apk  /opt/node/

appium
