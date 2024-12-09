## Lamarck &nbsp; &nbsp; &nbsp; 2024-11-08

---

*nwk文件添加日期标签*

> iqtree跑出来的数文件默认是treefile格式的，可以直接改后缀变成nwk文件。但是这个nwk文件是没有日期标签的，只有每个结点的遗传距离，可以通过一个python脚本给nwk文件添加这个日期标签，添加前和添加后的效果见下图（都只截取了文件中一小部分）：
 
**原始的nwk**
```
LT909545.1:0.0207688725,((((((((((((((LT909529.1:0.0001693356,LT909542.1:0.0000010049)95:0.0002545066,LT909535.1:0.0000850063)100:0.0090524866,KF155001.1:0.0107108846)100:0.0124115295,((LT909551.1:0.0067469444,KP723638.1:0.0117146535)100:0.0064501481,LT909531.1:0.0145969254)100:0.0150323840)96:0.0012283552
```

**处理后nwk**
```
(LT909545.1|2006-6-1:0.0207688725,((((((((((((((LT909529.1|1984-6-12:0.0001693356,LT909542.1|1984-8-18:0.0000010049)95:0.0002545066,LT909535.1|1989-2-13:0.0000850063)100:0.0090524866,KF155001.1|2009-1-1:0.0107108846)100:0.0124115295,((LT909551.1|1992-5-29:0.0067469444,KP723638.1|2014-7-11:0.0117146535)100:0.0064501481,LT909531.1|1993-1-25:0.0145969254)100:0.0150323840)96:0.0012283552,
```

```python
import re

# 读取日期文件并创建字典
date_dict = {}
with open(r"C:\Users\Lamarck\Desktop\test\name_date.txt", "r") as f:
    for line in f:
        if line.strip():  # 跳过空行
            parts = line.strip().split()
            sequence_id = parts[0]
            date = parts[1]
            date_dict[sequence_id] = date

# 读取并修改NWK文件
with open(r"C:\Users\Lamarck\Desktop\test\genome_1774.fasta.nwk", "r") as f:
    nwk_content = f.read()

# 匹配序列ID并添加日期
for seq_id, date in date_dict.items():
    # 使用正则表达式查找并替换每个节点的序列ID
    nwk_content = re.sub(rf"({seq_id})([\):])", rf"\1|{date}\2", nwk_content)

# 保存修改后的NWK文件
with open(r"C:\Users\Lamarck\Desktop\test\genome_1774_with_dates.nwk", "w") as f:
    f.write(nwk_content)

print("修改完成：带有日期标签的NWK文件已保存。")

```

**用插值表达式提取日期**

> \b\d{4}-\d{1,2}-\d{1,2}\b