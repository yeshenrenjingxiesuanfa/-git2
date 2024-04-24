# 《大数据技术在短视频评论区开源情报分析中的应用》项目简介

## 功能简介

该系统实现了以下功能：

1.从远端数据库中读取评论区数据（主要是中文文本）

2.并进行清洗和预处理（剔除非中文字符）

3.检查是否有敏感关键词，然后进行标记。

## 工程架构

系统完全采用python3.8进行开发，以下是工程文件架构：

```sh
    .
    ├── DB_operation.py  # 数据库相关操作（连接库和从库中读取文本）
    ├── README.md 		# 项目简介文件
    ├── dic_operation.py # 敏感词典相关操作（包括文本预处理和文本关键词对比）
    ├── main.py			# 项目主调函数
    ├── requirements.txt  # python 依赖包清单
    └── violence.txt  # 以文本形式保存的敏感词典文件（主要是暴恐相关违禁词）
```



## 环境配置

#### 1.安装python3.8及以上版本的解释器

如果有conda可以使用以下命令自动安装python3.8环境

```sh
conda create -n contentCensor python=3.8
```

激活conda环境

```sh
conda activate contentCensor
```

#### 2.使用pip安装工程所需要的依赖包

```sh
pip install -i requirements.txt
```



## 代码运行