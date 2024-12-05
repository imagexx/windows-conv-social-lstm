# import torch
#
# if torch.cuda.is_available():
#     print("CUDA is available! You can use GPU for computation.")
# else:
#     print("CUDA is not available. Computation will be on CPU.")

import torch
print(torch.cuda.is_available())  # 应该返回 True
print(torch.__version__)  # 确认正确版本安装
print(torch.version.cuda)  # 查看CUDA版本

# import torch
#
# print("PyTorch version:", torch.__version__)
# print("Is CUDA available:", torch.cuda.is_available())
# if torch.cuda.is_available():
#     print("CUDA Device Name:", torch.cuda.get_device_name(0))