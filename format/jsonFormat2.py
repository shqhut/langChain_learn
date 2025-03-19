import json

# 从文件中读取 JSON 数据
input_file = "/Users/wayz/Desktop/城市网格数据/shanghai_geohash6_list.json"  # 输入文件名
output_file = "/Users/wayz/Desktop/城市网格数据/shanghai_geohash6_list_new.geojson"  # 输出文件名
geohash_data_file = "/Users/wayz/Desktop/城市网格数据/resident_heat_map_sh.json"  # 包含 geohash 和 residentCount 的文件

# 读取主 JSON 文件
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)  # 将文件内容解析为 JSON 对象

# 读取 geohash 数据文件
with open(geohash_data_file, "r", encoding="utf-8") as file:
    geohash_data = json.load(file)  # 将文件内容解析为 JSON 对象

# 将 geohash 数据转换为字典，方便快速查找
geohash_dict = {item["geohash"]: item["residentCount"] for item in geohash_data}

# 在 properties 中增加 count 属性，并根据 geohash 匹配值
for feature in data["features"]:
    geohash = feature["properties"]["name"]  # 假设 geohash 存储在 name 字段中
    if geohash in geohash_dict:
        feature["properties"]["count"] = geohash_dict[geohash]  # 匹配并设置 count 值
    else:
        feature["properties"]["count"] = 0  # 如果没有匹配到，设置默认值为 0

# 将修改后的 JSON 数据写入文件
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)  # 将 JSON 对象写入文件，并格式化输出

print(f"修改后的 JSON 数据已写入文件：{output_file}")