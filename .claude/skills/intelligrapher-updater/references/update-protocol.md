# 安全更新流程

1. **Backup**：在 `intelligrapher/references/backup/YYYYMMDD-HHMMSS/` 下备份原文件。
2. **Diff**：若文件已存在，生成变更摘要。
3. **Write**：按 schema-spec.md 写入新内容。
4. **Validate**：调用 `scripts/validate_structure.py` 检查。
5. **Rollback**：校验失败则从备份恢复。
