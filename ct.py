

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip()) #.strip 是去掉打印出来的\n 
	return lines

def convert(lines):

	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_sticker_count  = 0
	viki_image_count = 0

	for line in lines:
		s = line.split(' ') # 读取每个字串的时候，遇到空白键切割。
		time = s[0]
		name = s[1]

		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen传了', allen_word_count, '个字')
	print('allen传了', allen_sticker_count, '个贴图')
	print('allen传了', allen_image_count, '个图片')
	print('vikic说了', viki_word_count, '个字')
	print('vikic传了', viki_sticker_count, '个贴图')
	print('viki传了', viki_image_count, '个图片')
		# print(s)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt') #读取文件
	lines = convert(lines) 
	# write_file('output.txt', lines) #写入文件


main() #从下面开始