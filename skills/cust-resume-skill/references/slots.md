# 模板槽位规格与字数预算

## 为什么要卡字数

很多简历模板（尤其是设计感强的中文模板）是用 **Word 文本框**排的。文本框尺寸固定，**不会随内容自动撑开**——写长了会溢出或被裁掉，排版就乱了。

所以即使不自动生成 Word（手动粘贴），**字数预算依然是硬约束**。

⚠️ **不同模板差别很大，预算必须实测，不能照抄本文档的示例值。**

---

## 第一步：测量你自己的模板

对 docx 模板运行下面的脚本，把结果填进本文档的「槽位地图」。

```python
import zipfile, re
from xml.etree import ElementTree as ET

RESUME = '<你的简历路径>.docx'   # 见 config.md
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

z = zipfile.ZipFile(RESUME)
raw = re.sub(r'<mc:Fallback>.*?</mc:Fallback>', '',
             z.read('word/document.xml').decode('utf-8'), flags=re.S)
root = ET.fromstring(raw)

# 文本框排版
boxes = [e for e in root.iter() if e.tag.endswith('txbxContent')]
if boxes:
    for i, b in enumerate(boxes, 1):
        paras = [''.join(t.text or '' for t in p.iter(W+'t')) for p in b.iter(W+'p')]
        body = [p for p in paras if p.strip()]
        if not body: continue
        print(f'=== 槽位 {i} | {len(body)} 段 | {sum(len(x) for x in body)} 字 ===')
        for l in body:
            print(f'  [{len(l):>3}] {l[:60]}')
else:
    # 普通段落排版
    for p in root.iter(W+'p'):
        t = ''.join(x.text or '' for x in p.iter(W+'t'))
        if t.strip(): print(f'[{len(t):>3}] {t[:60]}')
```

> ⚠️ 必须先去掉 `mc:Fallback` 分支，否则文本框会被重复统计（一个框数成两个）。

## 第二步：检查 run 结构

决定「能不能只换字、不动版」的关键。

```python
for pi, p in enumerate(boxes[N].iter(W+'p')):     # N = 你要检查的槽位
    runs = [r for r in p.iter(W+'r')]
    txt = ''.join(t.text or '' for t in p.iter(W+'t'))
    if not txt.strip(): continue
    print(f'段{pi}: {len(runs)} 个 run | {txt[:28]}…')
    for r in runs[:6]:
        t = ''.join(x.text or '' for x in r.iter(W+'t'))
        rPr = r.find(W+'rPr')
        bold = rPr is not None and rPr.find(W+'b') is not None
        print(f'    run[粗={int(bool(bold))}] {t[:30]!r}')
```

**常见的 bullet run 模式**：

```
run1「▸」 + run2「 」 + run3「粗体标签：」 + run4「正文」
                          ↑加粗            ↑不加粗
```

如果是这个模式，**只替换 run4 的文字、其余一律不碰**，排版就 100% 不会动。

---

## 槽位地图（← 填入你的实测结果）

| 槽位 | 内容 | 现有字数 | 可改性 |
|---|---|---|---|
| 1 | 例：实习标题 + 公司抬头 + 工作概述 | 概述 XX 字 | 高价值，必改 |
| 2 | 例：排版残留的空标题 | — | 不动 |
| 3 | 例：校园经历 N 条 | 每条 XX–XX 字 | 可增删条目 |
| … | | | |

### 逐条现状（示例格式）

| 条目 | 现有字数 | 预算 |
|---|---|---|
| ▸ 标签A | 100 | 90–105 |
| ▸ 标签B | 68 | 60–80 |

**通用经验值**（仅供起步参考，务必以实测为准）：
- 中文 bullet 中位数 **60–70 字**
- 单条**不要超过全篇最长的那条**——那条已经是文本框的物理上限

---

## 输出格式

P5 输出的第一份文件按槽位组织，每条标字数：

```markdown
## 槽位 6 · 意向岗
意向岗：<按 JD 的岗位名>                [8字 / 预算 28]
所在地：<城市>                          [6字 / 预算 14]

## 槽位 1 · 工作概述
▸ **工作概述：**……                      [78字 / 预算 80]

## 槽位 9 · 实习经历
▸ **<标签>：**……                        [96字 / 预算 90-105]
...
```

**超预算的条目必须压缩后再输出，不能带着超标交付。**

---

## 每版都要检查的两处

1. **意向岗** —— 校招 / 社招 / 实习写错会直接投错池子。按 `config.md` 里的求职类型 + JD 的岗位名写
2. **经历标题的取景框** —— 同一段经历在不同岗位下标题应该不同。例：一段展会翻译经历，投销售岗时写「国际展会商务接待」比写「志愿者」有效得多
