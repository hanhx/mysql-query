# MySQL Query Skill

专业的 MySQL 只读查询工具，用于数据库检查、验证和调试。支持 Python 和 Shell 两种方式。

## 特性

- ✅ **只读安全**: 只允许 SELECT, DESCRIBE, SHOW, EXPLAIN 等查询
- 🔒 **安全防护**: 自动拒绝 INSERT, UPDATE, DELETE, DROP 等写操作
- 🐍 **Python 支持**: 使用 pymysql，无需安装 MySQL 客户端
- 🐚 **Shell 支持**: 传统 mysql 命令行工具（需要安装）
- 📊 **格式化输出**: 表格形式展示查询结果

## 安装依赖

### Python 方式（推荐）
```bash
pip3 install pymysql
```

### Shell 方式（可选）
```bash
# macOS
brew install mysql-client

# Ubuntu/Debian
sudo apt-get install mysql-client
```

## 使用方法

### Python 方式（推荐）

```bash
python3 scripts/query.py "SQL查询" 主机 端口 数据库名 用户名 [密码]
```

**示例：**

```bash
# 1. 查看所有数据库
python3 scripts/query.py "SHOW DATABASES" \
  your-host 3306 information_schema username password

# 2. 查看表结构
python3 scripts/query.py "DESCRIBE your_table" \
  your-host 3306 your_database username password

# 3. 查看特定列（支持通配符）
python3 scripts/query.py "SHOW COLUMNS FROM your_table LIKE 'prefix_%'" \
  your-host 3306 your_database username password

# 4. 查询数据
python3 scripts/query.py "SELECT * FROM your_table LIMIT 5" \
  your-host 3306 your_database username password

# 5. 查看所有表
python3 scripts/query.py "SHOW TABLES" \
  your-host 3306 your_database username password

# 6. 查看表的索引
python3 scripts/query.py "SHOW INDEX FROM your_table" \
  your-host 3306 your_database username password
```

### Shell 方式

```bash
bash scripts/query.sh "SQL查询" 主机 端口 数据库名 用户名 [密码]
```

## 常用查询示例

### 检查表结构
```bash
# 查看表的所有字段
python3 scripts/query.py "DESCRIBE table_name" host 3306 database user pass

# 查看特定字段
python3 scripts/query.py "SHOW COLUMNS FROM table_name WHERE Field='column_name'" host 3306 database user pass
```

### 验证字段是否存在
```bash
# 方法1: 使用 DESCRIBE
python3 scripts/query.py "DESCRIBE table_name" host 3306 database user pass | grep field_name

# 方法2: 使用 SHOW COLUMNS
python3 scripts/query.py "SHOW COLUMNS FROM table_name LIKE 'field_pattern%'" host 3306 database user pass

# 方法3: 查询数据
python3 scripts/query.py "SELECT field_name FROM table_name LIMIT 1" host 3306 database user pass
```

### 查看数据库信息
```bash
# 查看所有数据库
python3 scripts/query.py "SHOW DATABASES" host 3306 information_schema user pass

# 查看所有表
python3 scripts/query.py "SHOW TABLES" host 3306 database user pass

# 查看表的创建语句
python3 scripts/query.py "SHOW CREATE TABLE table_name" host 3306 database user pass
```

## 安全特性

### 允许的查询类型
- ✅ `SELECT` - 查询数据
- ✅ `DESCRIBE` / `DESC` - 查看表结构
- ✅ `SHOW` - 显示数据库、表、列等信息
- ✅ `EXPLAIN` - 查看查询执行计划

### 禁止的操作
- ❌ `INSERT` - 插入数据
- ❌ `UPDATE` - 更新数据
- ❌ `DELETE` - 删除数据
- ❌ `DROP` - 删除表/数据库
- ❌ `CREATE` - 创建表/数据库
- ❌ `ALTER` - 修改表结构
- ❌ `TRUNCATE` - 清空表

## 参数说明

| 参数 | 说明 | 必填 | 默认值 |
|------|------|------|--------|
| SQL查询 | 要执行的 SQL 语句 | ✅ | - |
| 主机 | MySQL 服务器地址 | ✅ | localhost |
| 端口 | MySQL 端口 | ✅ | 3306 |
| 数据库名 | 数据库名称 | ✅ | - |
| 用户名 | MySQL 用户名 | ✅ | - |
| 密码 | MySQL 密码 | ❌ | 空 |

## 输出格式

查询结果以表格形式展示：

```
Field | Type | Null | Key | Default | Extra
----------------------------------------------
id | bigint(20) | NO | PRI | None | auto_increment
name | varchar(100) | NO |  |  | 
status | int(11) | YES |  | None | 
created_at | timestamp | NO |  | CURRENT_TIMESTAMP | 
```

## 故障排查

### Python 方式
```bash
# 检查 pymysql 是否安装
pip3 list | grep pymysql

# 安装 pymysql
pip3 install pymysql
```

### Shell 方式
```bash
# 检查 mysql 客户端是否安装
which mysql

# macOS 安装
brew install mysql-client

# Ubuntu/Debian 安装
sudo apt-get install mysql-client
```

## 最佳实践

1. **使用只读账号**: 建议使用只有 SELECT 权限的数据库账号
2. **限制查询范围**: 使用 LIMIT 限制返回结果数量
3. **保护密码**: 避免在命令历史中暴露密码
4. **测试环境优先**: 先在测试环境验证查询语句

## 示例：验证字段是否添加成功

```bash
# 完整示例：验证字段是否存在
python3 scripts/query.py \
  "SHOW COLUMNS FROM your_table LIKE 'field_prefix_%'" \
  your-host \
  3306 \
  your_database \
  your_username \
  your_password
```

## 贡献

欢迎提交 Issue 和 Pull Request！
