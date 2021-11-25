import os
while True:
	a = input("xray启动后，输入任意字符并按回车确认开始探测：")
	if not a :
		pass
	else:
		break
for i in open('url.txt','r'):
	i = i[:-1]
	if "http" not in i:
		i = "http://" + i
	command = "rad_windows_amd64.exe  -t " + i + " -http-proxy 127.0.0.1:7777"
	print('开始扫描：'+i)
	try:
		os.system(command)
	except Exception as e:
		print('扫描异常...')
		pass

print('全部扫描完毕！')

