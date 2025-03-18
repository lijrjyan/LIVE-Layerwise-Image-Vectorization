import torch
print(torch.cuda.is_available())  # 需要返回 True
print(torch.cuda.get_device_name(0))  # 需要显示你的 GPU，例如 "Tesla T4"

