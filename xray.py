import os
from threading import Thread
from time import sleep
import win32api 
#判断文件名是否正确
while True:
	filename = input('请输入要保存的文件名：')
	if ":"  in filename:
		print("您输入不是文件名，请重新输入")
	else:
		break

filename = r".\result\\" + filename + ".html"
if os.path.exists(filename):
	try:
		os.remove(filename)
	except:
		print("删除旧文件失败")
command = "xray_windows_amd64.exe webscan --listen 127.0.0.1:7777 --html-output " + filename
print("命令为：",command)

com = [command,filename]
def xray(command):
	try:
		os.system(command)
	except:
		pass

def html(filename):
	while True:
		sleep(10)
		if os.path.exists(filename):
			try:
				win32api.ShellExecute(0, 'open', filename, '', '', 1)
			except:
				print('自动打开xray扫描报告出错')
			break
def main():
	try:
		for s in com:
			if "64.exe" in s:
				t = Thread(target=xray,args=(s,))
				t.start()
			if "html" in s:
				t = Thread(target=html,args=(s,))
				t.start()
	except:
		pass
if __name__ == '__main__':
	main()