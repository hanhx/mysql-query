# MySQL Query Skill

[![GitHub](https://img.shields.io/badge/GitHub-hanhx%2Fmysql--query-blue?logo=github)](https://github.com/hanhx/mysql-query)

让 AI IDE（Windsurf / Cursor）直接在终端查询 MySQL，适合代码开发后的数据核对、结构检查和联调验证。

---

## 快速开始（1 分钟）

### 1) 安装到 AI IDE

**方式 A：直接安装（推荐，最省事）**

```bash
# Windsurf
git clone https://github.com/hanhx/mysql-query.git ~/.codeium/windsurf/skills/mysql-query

# Cursor
git clone https://github.com/hanhx/mysql-query.git ~/.cursor/skills/mysql-query
```

**方式 B：已在本地有仓库时，用软链接**

```bash
# Windsurf
ln -s /path/to/mysql-query ~/.codeium/windsurf/skills/mysql-query

# Cursor
ln -s /path/to/mysql-query ~/.cursor/skills/mysql-query
```

安装完成后，IDE 会自动识别 `SKILL.md` 并加载该 skill。

> 首次执行查询时，如果本机未安装 `pymysql`，skill 会自动安装（等价于 `python -m pip install pymysql`），无需手动执行。
> 如在受限环境不希望自动安装，可先设置：`export MYSQL_QUERY_AUTO_INSTALL=0`。

### 2) 配置数据库连接（首次查询前完成）

```bash
cp config.example.json config.json
```

编辑 `config.json`，至少配置一个连接（例如 `bcm-test`）。

`connections.<name>` 下字段说明：
- 必填：`host`、`port`、`database`、`username`、`password`
- 可选：`description`、`project_path`、`keywords`

```json
{
  "connections": {
    "bcm-test": {
      "host": "your-host",
      "port": 3306,
      "database": "your_database",
      "username": "your-username",
      "password": "your-password",
      "description": "测试环境",
      "project_path": "/path/to/your/project",
      "keywords": ["bcm", "test"]
    }
  }
}
```

---

## 在聊天里怎么用

配置好后，直接对 AI 说：

> "帮我查一下 test 环境 user 表结构"

> "查一下 test 库 order 表最近 10 条数据"

> "确认一下 xxx 字段是否已经上线到表结构"

AI 会自动调用 skill 执行查询并返回结果。

---

## 写完代码后自动查库验证

这个 skill 的推荐用法是：**写代码 → 查库验证 → 再调整**。

你可以直接这样说：

> "帮我给 order 表加一个 status 字段，加完后查表结构确认"

> "写一个按用户 ID 查询订单的接口，完成后查几条数据验证 SQL 是否正确"

> "重构这段查询逻辑，改完后帮我查库核对结果"

---

## 手动命令（排障用）

```bash
# 用配置名查询（推荐）
python3 scripts/query_with_config.py -c test "SHOW TABLES"
python3 scripts/query_with_config.py -c test "SELECT * FROM your_table LIMIT 5"

# 直接传连接参数
python3 scripts/query.py "SHOW TABLES" host 3306 database user password
```

---

## 安全与默认行为

- **只读限制**：仅允许 `SELECT / DESCRIBE / SHOW / EXPLAIN`
- **自动限流**：`SELECT` 未写 `LIMIT` 时自动追加 `LIMIT 10`
- **自动安装可控**：默认自动安装 `pymysql`；设置 `MYSQL_QUERY_AUTO_INSTALL=0` 可关闭
- **敏感配置隔离**：`config.json` 已在 `.gitignore`，不会被提交
- **建议**：使用只读数据库账号

---

## 常见问题

### 1) 为什么查出来只有 10 条？
因为 `SELECT` 未带 `LIMIT` 时会自动补 `LIMIT 10`。如果你需要更多数据，请显式写：

```sql
SELECT * FROM your_table LIMIT 100;
```

### 2) 为什么某些 SQL 被拒绝？
该 skill 是只读模式，`INSERT/UPDATE/DELETE/DDL` 都会被拦截。

### 3) AI 提示连接失败怎么办？
检查：
1. `config.json` 中 host/port/database/username/password 是否正确
2. 数据库网络是否可达（办公网/VPN）
3. 账号是否有目标库的只读权限
