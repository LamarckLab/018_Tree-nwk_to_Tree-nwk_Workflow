<h1 align="center">🧬 给 Newick 树添加日期标签</h1>

<p align="center"><em>—— 用 Python 给 .nwk 树的叶节点批量追加采样日期</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Field-Phylogenetics-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Cross--platform-555?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square" />
</p>

---

## 项目背景

IQ-TREE 跑出的 treefile 改后缀即为 .nwk，但只有遗传距离、没有采样日期。本脚本按「序列名 → 日期」对照表，给 .nwk 里每个叶节点名追加 `|日期`，便于后续做时间树 / 时间轴可视化。

## 输入格式

- `name_date.txt`：制表符分隔，首行表头 `Name<TAB>Date`，其后每行一个「序列名  日期(YYYY-M-D)」
- `tree.nwk`：待处理的 Newick 树

示例见 [Input Format/](./Input%20Format)。

## 效果示例

**原始 nwk**（只有遗传距离）
```
LT909545.1:0.0207688725,((((((((((((((LT909529.1:0.0001693356,LT909542.1:0.0000010049)95:...
```

**处理后 nwk**（叶名追加 `|日期`）
```
LT909545.1|2006-6-1:0.0207688725,((((((((((((((LT909529.1|1984-6-12:0.0001693356,LT909542.1|1984-8-18:...
```

## 用法

编辑 [nwk_transform.py](./nwk_transform.py) 顶部三处路径（`name_date.txt`、输入 `tree.nwk`、输出 `tree_dates.nwk`），然后运行：
```bash
python nwk_transform.py
```

> 提取日期的正则：`\b\d{4}-\d{1,2}-\d{1,2}\b`
