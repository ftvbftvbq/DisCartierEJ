#!/usr/bin/env python
# -*- coding: utf-8 -*-

# stf_url address
STF_URL = "http://xx.xx.xxx.xx:7100/api/v1/devices"

"""
access token of stf

STF uses OAuth 2.0 for authentication. In order to use the API,
you will first need to generate an access token. Access tokens
can be easily generated from the STF UI. Just go to the Settings
tab and generate a new access token in Keys section.
Don't forget to save this token somewhere, you will not be able to see it again.
"""
TOKEN = "3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421"

STF_DELETE_URL = "http://xxx.xxx.xxx.xx:7100/api/v1/user/devices/"

# some variables in desired_capablities
PLATFORM_NAME = 'Android'
NEW_COMMAND_TIMEOUT = 60
# the apk place in container
APK_NAME = "/apk_shell/xxx.apk"
# come infomation needed by docker_compose.yml
APPIUM_CARTIEREJ_IMAGE = "xxxxxx"
PORTS = 4723
APPIUM_CARTIEREJ_CMD = "bash /app_shell/app.sh"
APP_APK_VOLUMES = "xxxxxx:/apk_shell"

"""
Use device name as directory to save docker_compose.yml and app.sh
Need abs path
"""
DOCKER_COMPOSE_VOLUMES = "xxxxx/resources/dockercomposes/"

# logs save place in local
LOCAL_LOG_DIR = "xxxxx"
APPIUM_CARTIEREJ_LOGS_VOLUMES = LOCAL_LOG_DIR + 'RANDOM:/opt/node/CartierEJ/logs'  # RANDOM为变量在生成的过程中替换

# case to run
CASE_NAME = "test_login.py"