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
