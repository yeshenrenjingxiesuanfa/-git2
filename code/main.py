import DB_operation
import dic_operation 

DB_operation.DB.connectDB()
# processed_text = dic_operation.dic.preprocess(DB_operation.DB.current_text)
dic_operation.dic.openDic(dic_operation.dic_filename, dic_operation.dic_words)
dic_operation.dic.matchKey(DB_operation.DB.table_info,dic_operation.dic_words)