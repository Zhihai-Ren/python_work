#动物识别系统
import os
from Inference_engine import Inference_engine

#特征
len = [x for x in range(1, 25)]
#path为此py文件所在路径
path = os.getcwd()
#知识库路径
knowledge = str(path) + "\knowledge.txt"
#规则库路径
rule = str(path) + "\\rule.txt"
f = open(knowledge, 'r')
information = f.read()
f.close
b = eval(information[-59:])
animal = list(b.values())
print("------------------------动物识别系统------------------------")
print("此系统可以识别以下几种动物：")
print(list(b.keys()))
print("从以下特征中选择已知条件：")
print(information[0:-59])

#开始推理
while True:
	known_conditions = \
		input("已知条件有（输入对应的序号，使用空格分隔序号）：")
	known_conditions = known_conditions.split()
	known_conditions = [int(x) for x in known_conditions]
	result = Inference_engine(known_conditions, rule, len, animal)
	if result == -1:
		print("已知已知条件不在上述特征范围内")
	if result == 0:
		print("根据已知条件和规则不能推理出具体的动物")
	else:
		a = b
		str2 = "推理出的动物是："+str(list(a.keys())[list(a.values()).index(result)])
		print(str2)
	
	#是否按下*键，按下结束程序
	print("按回车继续，按*退出")
	a = input()
	if a == '*':
		break
#推理_end