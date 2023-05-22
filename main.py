import os
import pandas as pd
import sqlalchemy

# 连接到数据库
def connect_to_database(connection_str):
    return sqlalchemy.create_engine(connection_strconnect()

# 获取数据库中的表和列信息
def get_tables_and_columns(connection):
    inspector = sqlalchemy.inspect(connection)
    tables = inspector.get_table_names()
    table_info = {}
    for table in tables:
        columns = inspector.get_columns(table)
        table_comment = inspector.get_table_comment(table)
        table_info[table] = {
            'columns': columns,
            'comment': table_comment['text'] if table_comment['text'] else table
        }
    return table_info

# 将数据保存到文件
def save_data_to_files(connection, table_info):
    # 创建输出目录
    os.makedirs('数据', exist_ok=True)
    os.makedirs('数据1', exist_ok=True)

    for table, info in table_info.items():
        columns = info['columns']
        # 获取列注释
        column_comments = [column['comment'] if column['comment'] else column['name'] for column in columns]

        # 查询表数据
        query = f"SELECT * FROM {table}"
        data = pd.read_sql(sql=query, con=connection)
        # 重命名列名为注释
        data.columns = column_comments

        # 保存数据到文件
        filename = info['comment']
        data.to_pickle(os.path.join('数据', f"{filename}.pkl"))
        data.head().astype('str').to_excel(os.path.join('数据1', f"{filename}.xlsx"), index=False)
        print(filename)

def main():
    # 数据库连接字符串
    db_connection_str = 'mysql+pymysql://root:root@host/databases?charset=utf8'
    # 连接到数据库
    connection = connect_to_database(db_connection_str)
    # 获取表和列信息
    table_info = get_tables_and_columns(connection)
    # 保存数据到文件
    save_data_to_files(connection, table_info)
    # 关闭数据库连接
    connection.close()

if __name__ == '__main__':
    main()
