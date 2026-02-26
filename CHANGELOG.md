# MySQL Query Skill - 更新日志

## v1.0.0 (2026-02-26)

### 🎉 初始版本

#### 功能特性
- ✅ Python 查询脚本（使用 pymysql）
- ✅ Shell 查询脚本（使用 mysql 客户端）
- ✅ 配置文件支持（保存常用数据库连接）
- ✅ 安全防护（只允许只读查询）
- ✅ 格式化输出（表格形式）

#### 文件结构
```
mysql-query/
├── SKILL.md                      # Skill 说明文档
├── README.md                     # 详细使用文档
├── CHANGELOG.md                  # 更新日志
├── .gitignore                    # Git 忽略配置
├── config.example.json           # 配置文件示例
├── config.json                   # 实际配置（需自行创建）
└── scripts/
    ├── query.py                  # Python 查询脚本
    ├── query_with_config.py      # 支持配置文件的查询脚本
    └── query.sh                  # Shell 查询脚本
```

#### 安全特性
- 只允许 SELECT, DESCRIBE, SHOW, EXPLAIN 查询
- 自动拒绝 INSERT, UPDATE, DELETE, DROP 等写操作
- 支持只读数据库账号

#### 使用示例
```bash
# 使用配置文件
python3 scripts/query_with_config.py --config test "DESCRIBE table_name"

# 直接指定参数
python3 scripts/query.py "SELECT * FROM table LIMIT 5" host 3306 db user pass
```

#### 实际应用
- ✅ 成功验证 BCM 项目的 `cell_series_count` 和 `cell_parallel_count` 字段
- ✅ 连接到测试数据库 `pe_battery_circulation_management_test`
- ✅ 查询表结构并验证字段存在

### 依赖
- Python 3.x
- pymysql (pip3 install pymysql)
- mysql-client (可选，用于 Shell 脚本)

### 贡献者
- Cascade AI Assistant

---

## 未来计划

### v1.1.0
- [ ] 支持查询结果导出（CSV, JSON）
- [ ] 添加查询历史记录
- [ ] 支持多数据库并行查询
- [ ] 添加查询性能分析

### v1.2.0
- [ ] 支持 PostgreSQL
- [ ] 支持 SQLite
- [ ] Web UI 界面
- [ ] 查询结果可视化
