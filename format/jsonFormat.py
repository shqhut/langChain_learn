import json

# 从文件中读取 JSON 数据
input_file = "/Users/wayz/Desktop/shanghai_geohash6_list.json"  # 输入文件名
output_file = "/Users/wayz/Desktop/shanghai_geohash6_list_1.json"  # 输出文件名

# 读取文件内容
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)  # 将文件内容解析为 JSON 对象

# 在 properties 中增加 count 属性
for feature in data["features"]:
    feature["properties"]["count"] = 0  # 设置默认值为 0

# 将修改后的 JSON 数据写入文件
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)  # 将 JSON 对象写入文件，并格式化输出

print(f"修改后的 JSON 数据已写入文件：{output_file}")