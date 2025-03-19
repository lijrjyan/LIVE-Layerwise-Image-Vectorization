import os
import subprocess
import concurrent.futures

# 配置参数
config_file = "config/base.yaml"
experiment = "experiment_5x1"
log_dir = "log/"
figures_dir = "figures/"
max_workers = 4  # 并行任务数

# 获取 figures 目录下的所有 png 文件
png_files = [f for f in os.listdir(figures_dir) if f.endswith(".png")]

def run_command(target_file):
    """执行 Python 命令"""
    target_path = os.path.join(figures_dir, target_file)
    signature = os.path.splitext(target_file)[0]  # 获取文件名（去掉 .png 扩展名）
    
    command = [
        "python", "main.py",
        "--config", config_file,
        "--experiment", experiment,
        "--signature", signature,
        "--target", target_path,
        "--log_dir", log_dir
    ]
    
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Success: {target_file}")
    else:
        print(f"Failed: {target_file}\nError: {result.stderr.decode()}")

# 并行执行任务
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(run_command, png_files)

print("All tasks submitted.")

