# crossborder-amazon-ads

离线优先的亚马逊广告诊断 Skill，面向跨境卖家和团队培训。

## 支持

- 广告结构诊断
- 预算与竞价复盘
- 搜索词与否定建议
- 报表质量检查
- 旺季/秒杀三段式联检

## 快速使用

```powershell
$env:PYTHONUTF8='1'
python scripts/ads_audit.py --input assets/sample-report.csv --mode all --output assets/sample-review.json
python C:/Users/admin/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

脚本只读本地 CSV/JSON，不连接 Amazon Ads API，不修改账户。缺失字段、实时政策、库存和收益结果统一标记为 `待确认`。

## 许可与来源

本目录的代码、模板和文案为本项目原创整理；公开资源只用于接口形态和流程研究，具体边界见 `references/source-map.md`。不包含原始课程视频、逐字稿、原作者水印或第三方 MCP 配置。
