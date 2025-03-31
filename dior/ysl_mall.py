import json
import csv
from pathlib import Path


def extract_mall_info_to_csv(json_file_path, csv_file_path=None):
    """
    从JSON文件提取商场编码和名称，保存为两列CSV

    参数:
        json_file_path: JSON文件路径
        csv_file_path: CSV输出路径(可选)
    """
    try:
        # 1. 读取JSON文件
        json_path = Path(json_file_path)
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 2. 提取商场编码和名称
        mall_info = []
        for store in data:
            mall_id = store.get('id', '')
            mall_name = store.get('detailInfo', {}).get('name', '')
            if mall_id and mall_name:  # 确保两个字段都有值
                mall_info.append([mall_id, mall_name])

        # 3. 设置默认输出路径
        if csv_file_path is None:
            csv_file_path = json_path.with_suffix('.csv')

        # 4. 写入CSV文件
        with open(csv_file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['商场编码', '商场名称'])  # 写入表头
            writer.writerows(mall_info)  # 写入数据

        print(f"成功提取 {len(mall_info)} 条商场数据")
        print(f"结果已保存到: {csv_file_path}")
        return True

    except FileNotFoundError:
        print(f"错误：文件 {json_file_path} 不存在")
    except json.JSONDecodeError:
        print(f"错误：文件 {json_file_path} 不是有效的JSON格式")
    except Exception as e:
        print(f"发生错误：{str(e)}")
    return False


# 使用示例
if __name__ == "__main__":
    # 示例1：自动生成同名CSV文件
    extract_mall_info_to_csv('../resource/ysl_2501.json')

    # 示例2：指定输出路径
    # extract_mall_info_to_csv('malls.json', 'mall_code_name.csv')