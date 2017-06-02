#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 本地存放logs的地址，每一个容器容器产生的logs都会映射到此文件夹下
LOCAL_LOG_DIR = "/Users/red/tmp/logs/"

# 需要将apk拷入到container内， 也可以再做image的时候，直接进行从网站下下载（最好的方法）
# 但是目前的"https://fir.im/viphk"还不支持
# 这里是直接映射过去的
# /Users/red/temp/appium/com.xingin.xhs-test-4.20.apk
APK_NAME = "/apk_shell/com.xingin.xhs-test-4.20.apk"
STF_URL = "http://10.12.144.16:7100/api/v1/devices"
TOKEN = "3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421"
STF_DELETE_URL = STF_URL + "/user/devices/"

# some variables in desired_capablities
PLATFORM_NAME = 'Android'
NEW_COMMAND_TIMEOUT = 60

# come infomation needed by docker_compose.yml
APPIUM_CARTIEREJ_IMAGE = "suifengdeshitou/liuwei:latest"
# APK_NAME = 'com.xingin.xhs-test-4.20.apk'
PORTS = 4723
APPIUM_CARTIEREJ_CMD = "bash /app_shell/app.sh"
APP_APK_VOLUMES = "/Users/red/temp/appium:/apk_shell"
# 每一个设备都会在dockercomposes文件夹下生产一个以设备名称命名的文件夹
DOCKER_COMPOSE_VOLUMES = "/Users/red/PycharmProjects/cartier_distributor/resources/dockercomposes/"
APPIUM_CARTIEREJ_LOGS_VOLUMES = LOCAL_LOG_DIR + 'RANDOM:/opt/node/CartierEJ/logs'  # RANDOM为变量在生成的过程中替换

# case to run
CASE_NAME = "test_login.py"