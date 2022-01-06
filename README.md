# xray-rad-
xray+rad实现批量自动化扫描，rad下载 》https://github.com/chaitin/rad

xray的被动扫描能力很强，但是主动扫描就弱了点，而rad的爬虫功能很强，所以将两种结合起来就能取长补短。但是它们两者不能进行批量检测。所以写了个脚本让两者结合进行批量检测。

首先将xray与rad所在文件夹加入到环境变量中，环境变量——用户变量——path——编辑

![image](https://user-images.githubusercontent.com/73785589/143380522-dc9a5510-1527-4c68-a628-d33460a1ba37.png)

使用的是python3，安装依赖库
pip install pypiwin32
pip isntall requests

注意，系统需要装有chrome浏览器
之后将要扫描的目标放在url.txt文件中，一个目标一行。接着点击xray批量自动检测.bat

启动后如下，输入xray扫描后的漏洞文件名，然后rad框中输入任意的数字 

![image](https://user-images.githubusercontent.com/73785589/143380572-06ebf313-6064-457f-90be-71b6711db3ae.png)

过程如下 

![image](https://user-images.githubusercontent.com/73785589/143380597-5a848ac8-d8d6-4070-8bb0-0879fc7093de.png)

 如果扫描出漏洞后会自动弹出浏览器漏洞报告
