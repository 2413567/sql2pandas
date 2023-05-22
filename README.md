# MySQL数据库表导出工具

这个Python脚本用于从MySQL数据库中导出数据表，并将其保存为pkl和Excel文件。

## 功能

1. 连接到MySQL数据库。
2. 获取数据库中的所有表名。
3. 遍历每个表名，读取数据并保存为pkl文件。
4. 为DataFrame设置字段名和注释。
5. 保存为pkl文件，以注释作为文件名。
6. 保存为Excel文件，以注释作为文件名。
7. 关闭数据库连接。

## 使用方法

1. 安装所需的库：

```bash
pip install pandas sqlalchemy pymysql openpyxl
```
2. 修改脚本中的数据库连接信息：
```
connection = sqlalchemy.create_engine('mysql+pymysql://root:root@host/data?charset=utf8').connect()
```
3. 运行脚本：
python export_tables.py
4. 在当前目录下，会生成两个文件夹：数据 和 数据1。数据 文件夹中包含pkl文件，数据1 文件夹中包含Excel文件。
注意事项
- 确保已安装所需的库。
- 根据实际情况修改数据库连接信息。
- 在运行脚本之前，确保当前目录下不存在名为数据和数据1的文件夹，以免覆盖现有数据。
 ## 请根据实际需求进行修改。
