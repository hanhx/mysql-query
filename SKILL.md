---
name: mysql-query
description: MySQL 只读查询工具 - 数据库检查、验证和调试
---

# MySQL Query Skill

专业的 MySQL 只读查询工具，支持数据库检查、验证和调试。

## 功能特性

- ✅ **只读安全**: 只允许 SELECT, DESCRIBE, SHOW, EXPLAIN 等查询
- 🔒 **安全防护**: 自动拒绝 INSERT, UPDATE, DELETE, DROP 等写操作
- 🐍 **Python 支持**: 使用 pymysql，无需安装 MySQL 客户端
- 🐚 **Shell 支持**: 传统 mysql 命令行工具
- 📊 **格式化输出**: 表格形式展示查询结果
- ⚙️ **配置管理**: 支持保存常用数据库连接配置

## 快速开始

### 1. 安装依赖
```bash
pip3 install pymysql
```

### 2. 配置数据库连接（可选）
```bash
cp config.example.json config.json
# 编辑 config.json，添加你的数据库连接信息
```

### 3. 执行查询

**使用配置文件（推荐）：**
```bash
python3 scripts/query_with_config.py --config test "DESCRIBE your_table"
```

**直接指定参数：**
```bash
python3 scripts/query.py "DESCRIBE your_table" host 3306 database user password
```

## 使用场景

### 1. 验证数据库字段是否添加
```bash
python3 scripts/query_with_config.py --config test \
  "SHOW COLUMNS FROM your_table LIKE 'field_prefix_%'"
```

### 2. 检查表结构
```bash
python3 scripts/query_with_config.py --config test \
  "DESCRIBE your_table"
```

### 3. 查看所有表
```bash
python3 scripts/query_with_config.py --config test \
  "SHOW TABLES"
```

### 4. 查询数据
```bash
python3 scripts/query_with_config.py --config test \
  "SELECT * FROM your_table LIMIT 5"
```

## 安全特性

### 允许的操作
- ✅ SELECT - 查询数据
- ✅ DESCRIBE/DESC - 查看表结构
- ✅ SHOW - 显示数据库信息
- ✅ EXPLAIN - 查看执行计划

### 禁止的操作
- ❌ INSERT/UPDATE/DELETE - 数据修改
- ❌ DROP/CREATE/ALTER - 结构修改
- ❌ TRUNCATE - 清空表

## 配置文件格式

```json
{
  "connections": {
    "test": {
      "host": "your-host",
      "port": 3306,
      "database": "your_database",
      "username": "your_username",
      "password": "your_password",
      "description": "测试环境"
    }
  }
}
```

## 文件说明

- `scripts/query.py` - Python 查询脚本（推荐）
- `scripts/query_with_config.py` - 支持配置文件的查询脚本
- `scripts/query.sh` - Shell 查询脚本（需要 mysql 客户端）
- `config.example.json` - 配置文件示例
- `config.json` - 实际配置文件（不会被 git 跟踪）

## 最佳实践

1. 使用只读权限的数据库账号
2. 将敏感信息保存在 config.json 中
3. 使用 LIMIT 限制查询结果数量
4. 优先在测试环境验证查询语句
