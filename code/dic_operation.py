# 该文件主要用于文本预处理、敏感词与评论区文本匹配
import re

# 敏感词典数据，以一个字符串数组方式保存。默认为空
dic_words = []
# 敏感词典文件名，一般以.txt文件保存
dic_filename = 'military.txt'

# 字符数组，用于存储预处理中的标点符号、阿拉伯数字和英文字母
preprocess_dic = ",，!！[]()\\"

# 定义词典处理类
class dic:
    # 记录该条评论是否违规。结果以布尔值存储。默认为True（违规）
    mark_illegal = True


    # 打开txt格式的敏感词典
    def openDic(filename, words):
        # 以中文编码方式打开敏感词典
        with open(filename, 'r', encoding='gbk') as file:
            for line in file:
                # 使用空格来分割每一行的文本，得到单词数组
                line_words = line.strip().split()
                # 将每一行的单词数组添加到总的单词列表中
                words.extend(line_words)
        print("\n敏感词条已被完全读取到程序中！")



    # 文本预处理函数
    def preprocess(rows):
        # 去除标点符号
        output = input.translate(str.maketrans('','',preprocess_dic))
        return output
    
    # 将敏感词典中的敏感词与读取到的评论区文本一一匹配。其中参数1为敏感词条数组，参数2为一条预处理过的评论区文本
    # 会重置该条文本的违规变量 mark_illegal
    # rows是表中读到的数据，sensiti_words是敏感词数组
    def matchKey(rows, sensitive_words):
        # 将词条拼接成正则表达式的形式，使用管道符号 | 分隔
        print("\n敏感词组为"+str(sensitive_words)+", 即将进行文本关键词匹配步骤！")
        # pattern = '|'.join(sensitive_words)
        # # 在词条的两边添加单词边界 \b
        # pattern = r'(?:' + pattern + r')'
        
        # # 在文本中查找匹配项
        # matches = re.findall(pattern, rows)
        # # 如果未找到匹配项，返回False（通过）；否则返回True（违规）

        for row in rows: # 遍历每一行
            comment = row[1] # 取索引为1的字段为评论区信息进行遍历
            for word in sensitive_words: # 遍历敏感词组
                if word in comment:
                    print(f"序号为'{row[0]}'的词条违规！，评论 '{comment}' 匹配到了敏感词 '{word}' ")

        # dic.mark_illegal = bool(matches)
        # if(dic.mark_illegal == False):
        #     print("\n该条评论通过！")
        # else:
        #     print("\n该条评论违规！违禁词条为"+str(matches)+"!")
