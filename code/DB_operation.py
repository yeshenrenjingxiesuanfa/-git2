# 该文件主要用于从数据库里提取评论区文本信息
import sqlalchemy
class DB:
    # 数据库连接信息
    host = "8.130.22.66"
    port = 3306
    user="gamedev"
    dbname = "gamedev"
    passwd ="gamedeveloper"
    # 将数据库信息写成可被 sqlalchemy 引擎配置的形式
    # 依次填写MySQL的用户名、密码、IP地址、端口、数据库名
    engine_cfg = "mysql+pymysql://"+user+":"+passwd+"@"+host+":3306/"+dbname
    # 查询语句
    query = "select comment_id, comment from test limit 10;"
    # 该变量用于存放当前读取的的文本，会被text_prepose.py和Dic_operation.py进行预处理和对比
    table_info = ""
    review_id = 1
    # 
    # 连接数据库
    def connectDB():
    # 打印sqlalchemy引擎配置信息
        print("\n数据库引擎信息为"+DB.engine_cfg)
        # 创建引擎
        engine = sqlalchemy.create_engine(DB.engine_cfg)
        with engine.connect() as con:
            # 执行查询语句
            result = con.execute(sqlalchemy.text(DB.query))
            # 获取查询结果的具体内容
            DB.table_info = result.fetchall()
            print("成功执行查表语句！已将表格信息保存到table_info变量中！")
            print("当前表格信息为"+str(DB.table_info))

    


    # 根据文本的违规结果，将记录写入数据库
    def write2table():
        print("write2table")
        