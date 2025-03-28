import json
import csv
from pathlib import Path


def extract_malls_to_csv(json_file_path, csv_file_path=None):
    """
    从JSON文件读取商场数据，提取所有商场名称，并写入CSV文件

    参数:
        json_file_path: JSON文件路径
        csv_file_path: 要保存的CSV文件路径（可选，默认与JSON文件同目录）
    """
    try:
        # 1. 读取JSON文件
        json_path = Path(json_file_path)
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # 2. 提取所有商场名称
        mall_list = [mall for city in data.values() for mall in city.values()]

        # 3. 设置默认CSV输出路径（如未指定）
        if csv_file_path is None:
            csv_file_path = json_path.with_suffix('.csv')

        # 4. 写入CSV文件（仅商场名称）
        with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # 写入商场名称，每行一个
            writer.writerows([[mall] for mall in mall_list])

        print(f"成功提取 {len(mall_list)} 个商场名称")
        print(f"结果已保存到: {csv_file_path}")
        return True

    except FileNotFoundError:
        print(f"错误：文件 {json_file_path} 不存在！")
    except json.JSONDecodeError:
        print(f"错误：文件 {json_file_path} 不是有效的JSON格式！")
    except Exception as e:
        print(f"发生错误：{str(e)}")
    return False


# 使用示例
if __name__ == "__main__":
    # 示例1：自动生成同名CSV文件
    extract_malls_to_csv('../resource/channl_mall.json', '../resource/channl_mall.csv')