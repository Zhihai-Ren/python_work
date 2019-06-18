def Inference_engine(known_conditions, rule, len, animal):
	# 检验已知条件是否合理
	for i in known_conditions:
		if i not in len:
			return -1
	
	f = open(rule, 'r')
	lines = f.readlines()
	f.close
	
	for line in lines:
		# 将规则处理为数字列表形式
		line = line.split()
		line = [int(x) for x in line]
		# 判断是否推理出新的条件
		result = 1  # 代表符合此条规则
		for i in line[0:-1]:
			if i not in known_conditions:
				result = 0
				break
		# 将新条件加入
		if result == 1:
			known_conditions.append(line[-1])
			print("推出了新条件：" + str(line[-1]))
			# 新推出的条件是具体动物时返回结果
			if line[-1] in animal:
				return line[-1]
	# 遍历完规则没有推出结果
	return 0
