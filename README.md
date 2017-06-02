# DisCartierEJ简介

作者：Juan Liu  @Date 2017/05/31

## DisCartierEJ是什么？
DisCartierEJ是一个可以将用户编写的case根据用户需要运行在不同设备（手机等）的框架。例如：用户编写了一个login的case，需要运行在 3 台 Version 高于 5.0 的设备上。

## 为什么有DisCartierEJ？
目前的一台设备上只能运行一个Appium，而一个Appium Server只能对应一个设备。在实践的过程中，常常需要一个case运行在不同类型不同版本的设备上，因而需要一个框架去支持这种需求。

## 为什么叫DisCariterEJ？
由于所有的case都是根据标准开发工具模板CartierEJ编写，因而称之为DisCariterEJ。

## DisCartierEJ的设计思路？
主要利用[STF](https://openstf.io/)(Smartphone Test Farm)来管理各种设备，利用[Docker](https://www.docker.com/)的[Docker-Compose](https://docs.docker.com/compose/)的工具生成满足各种需要的docker-compose.yml文件，一个docker-compose.yml文件对应一个包含case的Appium容器，一个包含case的Appium容器对应一个设备。

## 主要流程

1. DisCartierEJ根据用户的需求会给STF发送请求获取所需要的设备信息（返回的是一个JSON）。
2. 将返回来的信息注入到case中（利用docker-compose.yml模板中的环境变量，间接注入每一个包含case的Appium容器），实现一个包含case的Appium容器对应一个设备。
3. 在各个Appium内部运行case。

## 开发之前的准备
1.

## Demo演示

需求：需要将login整个CariterEJ运行在 3 台 Version 高于 5.0 的设备上。

步骤如下:

1. 编写login的CartierEJ代码（可以根据CartierEJ模块进行编写），在本地开发完并且验证成功，将CartierEJ中的contest.py中desired_capabilities中的信息替换成如下格式。

		@pytest.fixture(scope="session")
		def desired_caps(request):
		    """
		    	用于测试设备的效果
		    """
		    desired_caps = {}
		    desired_caps['platformName'] = 'Android'
		    try:
		        version = os.environ.get("PLATFORM_VERSION")
		        app_name = os.environ.get("APP_NAME")
		        devices_name = os.environ.get("DEVICES_NAME")
		    except KeyError:
		        logger.error("No environment variables for desired caps")
		        return None
		    if version is None or app_name is None or devices_name is None:
		        return None
		    desired_caps['platformVersion'] = version
		    desired_caps['app'] = app_name
		    desired_caps['deviceName'] = devices_name
		    desired_caps['newCommandTimeout'] = 60
		    desired_caps['unicodeKeyboard'] = 'true'
		    desired_caps['resetKeyboard'] = 'true'
		    desired_caps['noReset'] = 'false'
		    return desired_caps


2. 并将这些代码上传到github上或者一个可以从下载得到的代码，比如github地址为。

		https://github.com/haifengrundadi/CartierEJ.git

3. 将DisCartierEJ中的Dockerfile中的获取CartierEJ的代码更改为上面的地址。

		...
		#=======================================
		# pull code from git
		#=======================================
		RUN git clone https://github.com/haifengrundadi/CartierEJ.git
		WORKDIR CartierEJ
		RUN pip install -r requirements.txt & mkdir		WORKDIR tests/smoketest
		CMD ["bash /app_shell/app.sh]
		...

4. 使用Docker 根据Dockerfile 生成一个镜像文件 appium-cartierej-docker:latest
5. 将DisCartierEJ项目中的constant.py中相关变量替换为本地的实际信息。

		#!/usr/bin/env python
		# -*- coding: utf-8 -*-
		# 本地存放logs的地址，每一个容器容器产生的logs都会映射到此文件夹下
		LOCAL_LOG_DIR = "/Users/red/tmp/logs/"
		# 需要将apk拷入到container内， 也可以再做image的时候，直接进行从网站下下载（最好的方法）
		# 但是目前的"https://fir.im/viphk"还不支持
		# 这里是直接映射过去的
		APP_PATH = "/apk_shell/xxxxxx.apk"
		STF_URL = "http://xxx.xxx.xxx.xxx:7100/api/v1/devices"
		TOKEN = "3e5dd447cd334d549c849d19707eb269df74cabd67e5400986a5240023af6421"
		STF_DELETE_URL = STF_URL + "/user/devices/"
		# desired_capablities中的一些变量
		PLATFORMNAME = 'Android'
		TIMEOUT = 60
		# 生产docker_compose.yml需要的一些配置信息(不变的量）
		APPIUM_CARTIER_IMAGE = "suifengdeshitou/appium-cartier-docker:red"
		APK_NAME = 'xxxxxx.apk'
		PORTS = 4723
		APPIUM_CARTIER_CMD = "bash /app_shell/app.sh"
		APP_APK_VOLUMES = "/Users/red/temp/appium:/apk_shell"
		# 每一个设备都会在dockercomposes文件夹下生产一个以设备名称命名的文件夹
		DOCKER_COMPOSE_VOLUMES = "/Users/red/PycharmProjects/cartier_distributor/resources/dockercomposes/"
		APPIUM_CARTIER_LOGS_VOLUMES = LOCAL_LOG_DIR + 'RANDOM:/opt/node/cartier/logs'  # RANDOM为变量在生成的过程中替换
		# 要运行的case名称
		CASE_NAME = "test_create_notes.py"
6. 运行generator.py的 generator\_docker\_composes 方法会在dockercomposes文件夹下生成各种需要的文件。
7. 运行generator.py的 up\_docker\_composes 方法，会启动所有的容器，也就默认启动了容器中的所有case。