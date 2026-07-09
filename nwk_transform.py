import re

# 读取日期文件并创建字典
date_dict = {}
with open(r"C:\Users\Lamarck\Desktop\name_date.txt", "r") as f:
    for line in f:
        if line.strip():  # 跳过空行
            parts = line.strip().split()
            sequence_id = parts[0]
            date = parts[1]
            date_dict[sequence_id] = date

# 读取并修改NWK文件
with open(r"C:\Users\Lamarck\Desktop\tree.nwk", "r") as f:
    nwk_content = f.read()

# 匹配序列ID并添加日期
for seq_id, date in date_dict.items():
    # 使用正则表达式查找并替换每个节点的序列ID
    nwk_content = re.sub(rf"({seq_id})([\):])", rf"\1|{date}\2", nwk_content)

# 保存修改后的NWK文件
with open(r"C:\Users\Lamarck\Desktop\tree_dates.nwk", "w") as f:
    f.write(nwk_content)

print("修改完成：带有日期标签的NWK文件已保存。")
