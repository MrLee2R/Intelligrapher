---
name: intelligrapher-updater
description: Intelligrapher 的附属更新工具。当用户需要切换科研领域、初始化新领域知识库、更新期刊配色方案或补充学科绘图规范时触发。维护 intelligrapher 的知识库与审美库。
dependencies:
user-invocable: true
---

# Intelligrapher-updater

## Overview
维护 Intelligrapher 的「知识库」与「审美库」。通过结构化写入确保三库数据处于领域前沿。

## 支持的操作
1. **init**：初始化新领域骨架（在 intelligrapher/references/ 下创建 knowledge 和 aesthetic 模板文件）。
2. **switch**：切换默认领域（修改 `.current-domain` 标记文件）。
3. **update-knowledge**：基于用户提供的文献/规范，更新指定领域知识库。
4. **update-aesthetic**：基于目标期刊，更新配色与风格库。
5. **validate**：校验库文件结构是否符合 schema。

## 安全协议
- 更新前在 intelligrapher/references/backup/ 创建时间戳备份。
- 禁止直接修改 intelligrapher/assets/templates/（模板库由主 Skill 维护）。
- 新增领域必须遵循 `references/schema-spec.md` 的章节规范。

## 协作提示
更新完成后告知用户："知识库已更新至 ${target_domain}，现在可以调用 /intelligrapher 生成该领域科研绘图。"
