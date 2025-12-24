import qrcode
import os

# 定义所有二维码 (包含新增的 ArXiv)
codes = {
    "qr_web.png": "https://www.agent-kernel.tech/",
    "qr_git.png": "https://github.com/ZJU-LLMs/Agent-Kernel",
    "qr_rat.png": "https://www.bilibili.com/video/BV1dz2DBDERB",
    "qr_zju.png": "https://www.bilibili.com/video/BV1xamQBuEgS",
    "qr_arxiv.png": "https://arxiv.org/abs/2512.01610"  # 新增
}

# 保存路径 (建议直接改为您的桌面路径，省去移动步骤)
save_path = r"C:\Users\w1625\Desktop"

# 如果路径不存在，回退到当前目录
if not os.path.exists(save_path):
    save_path = "."
    print("未找到桌面路径，二维码将生成在当前脚本所在目录。请手动移动。")

def create_qr(filename, data):
    qr = qrcode.QRCode(version=1, box_size=10, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    # 使用深绿色填充
    img = qr.make_image(fill_color="#2E5728", back_color="white")
    
    full_path = os.path.join(save_path, filename)
    img.save(full_path)
    print(f"已生成: {full_path}")

print("正在更新二维码...")
for filename, url in codes.items():
    create_qr(filename, url)
print("所有二维码已准备就绪！")