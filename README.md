# MySQL Query Skill

[![GitHub](https://img.shields.io/badge/GitHub-hanhx%2Fmysql--query-blue?logo=github)](https://github.com/hanhx/mysql-query)

让 AI 编辑器（Windsurf / Cursor）直接查询 MySQL 数据库，只读安全，开箱即用。

## 快速开始

### 1. 安装依赖

```bash
pip3 install pymysql
```

### 2. 配置数据库连接

复制示例配置并填入你的数据库信息：

```bash
cp config.example.json config.json
```

编辑 `config.json`：

```json
{
  "connections": {
    "test": {
      "host": "your-host",
      "port": 3306,
      "database": "your_database",
      "username": "your-username",
      "password": "your-password",
      "description": "测试环境"
    }
  }
}
```

### 3. 安装到编辑器

将此目录软链到 skill 目录：

```bash
# Windsurf
ln -s $(pwd) ~/.codeium/windsurf/skills/mysql-query

# Cursor
ln -s $(pwd) ~/.cursor/skills/mysql-query
```

### 4. 开始使用

在聊天中直接告诉 AI：

> "帮我查一下 test 环境 user 表的结构"
>
> "查一下 test 库里 order 表最近 10 条数据"

AI 会自动调用 skill 执行查询。

## 手动使用

```bash
# 使用配置文件（推荐）
python3 scripts/query_with_config.py -c test "SHOW TABLES"
python3 scripts/query_with_config.py -c test "SELECT * FROM your_table LIMIT 5"

# 直接指定连接参数
python3 scripts/query.py "SHOW TABLES" host 3306 database user password
```

## 安全机制

脚本只允许只读查询，自动拒绝任何写操作：

- ✅ SELECT / DESCRIBE / SHOW / EXPLAIN
- ❌ INSERT / UPDATE / DELETE / DROP / CREATE / ALTER / TRUNCATE

## 注意事项

- `config.json` 包含敏感信息，已在 `.gitignore` 中排除，不会被提交
- 建议使用只读数据库账号
- 查询时加 `LIMIT` 避免返回过多数据
