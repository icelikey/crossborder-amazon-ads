# crossborder-amazon-ads

离线优先的亚马逊广告诊断 Skill，面向跨境卖家和团队培训。

支持广告结构诊断、预算与竞价复盘、搜索词否定建议、报表质量检查和旺季/秒杀联检。

## 快速使用

```powershell
$env:PYTHONUTF8='1'
python skill/scripts/ads_audit.py --input skill/assets/sample-report.csv --mode all --output skill/assets/sample-review.json
python C:/Users/admin/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill
```

脚本只读本地 CSV/JSON，不连接 Amazon Ads API，不修改账户。缺失字段、实时政策、库存和收益结果统一标记为 `待确认`。

本仓库只发布原创 Skill、模板和验证样例，不包含原始课程视频、逐字稿、原作者水印截图、第三方 MCP 配置或密钥。
## 配套运营 Skill：amazon-ops-codex

`amazon-ops-codex` 让 Codex 参与亚马逊运营的日常工作：读取导出、做日报与周报、诊断广告结构、整理搜索词、生成预算/竞价建议、安排旺季计划，并把每个动作写成可审计的决策记录。

它默认只读和提案模式；涉及广告、Listing、预算、竞价、否定词或外部发布的实际修改，必须由人对具体变更授权后再执行。

```powershell
$env:PYTHONUTF8='1'
python amazon-ops-codex/scripts/ops_intake_check.py --input amazon-ops-codex/assets/sample-ops-intake.json
python C:/Users/admin/.codex/skills/.system/skill-creator/scripts/quick_validate.py amazon-ops-codex
```

推荐调用：`Use $amazon-ops-codex to turn my Amazon exports into a daily or weekly operating brief.`
