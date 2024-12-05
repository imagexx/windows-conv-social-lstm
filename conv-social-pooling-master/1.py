# import pandas as pd
# from scipy.io import savemat
#
#
# # 读取 CSV 文件
# csv_file = 'F:/数据集/NGSIM/train.csv'
# df = pd.read_csv(csv_file)
#
#
#
# # 将 DataFrame 转换为字典，键为列名，值为对应的数据
# data_dict = df.to_dict(orient='list')
#
# # 保存为 .mat 文件
# mat_file = 'F:/数据集/NGSIM/train.mat'
# savemat(mat_file, data_dict)
#
# print(f"CSV 文件已转换并保存为 {mat_file}")
