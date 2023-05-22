import os.path
import pandas as pd
import sqlalchemy

# 连接MySQL数据库
connection = sqlalchemy.create_engine('mysql+pymysql://root:root@host/databases?charset=utf8').connect()

# 获取数据库中的所有表名
inspector = sqlalchemy.inspect(connection)
tables = inspector.get_table_names()

# 创建保存数据的目录（如果不存在）
os.makedirs('数据', exist_ok=True)
os.makedirs('数据1', exist_ok=True)

# 遍历每个表名，读取数据并保存为pkl文件
for table in tables:
    # 获取表结构信息
    columns = inspector.get_columns(table)
    table_comment = inspector.get_table_comment(table)

    # 解析字段名和注释
    column_names = [column['name'] for column in columns]
    column_comments = [column['comment'] if column['comment'] else column['name'] for column in columns]

    # 读取表数据
    query = f"SELECT * FROM {table}"
    query = sqlalchemy.text(query)
    data = pd.read_sql(sql=query, con=connection)

    # 为DataFrame设置字段名和注释
    data.columns = column_comments

    # 保存为pkl文件，以注释作为文件名
    filename = table_comment['text'] if table_comment['text'] else table
    data.to_pickle(os.path.join('数据', f"{filename}.pkl"))

    # 保存为Excel文件，以注释作为文件名
    data.head().astype('str').to_excel(os.path.join('数据1', f"{filename}.xlsx"), index=False)
    print(filename)

# 关闭数据库连接
connection.close()
