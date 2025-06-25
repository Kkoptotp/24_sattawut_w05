import os
from pathlib import Path

os_name = os.name
os_path = os.getcwd()
os_user = os.getenv("username")

# การทำงานใน path
current_path = Path.cwd()

# สร้างโฟนเดอร์
make_folder = current_path / "test123"
make_folder .mkdir(exist_ok=True)

# สร้างไฟล์
make_file = current_path / "test.ex"
# make_file.write_text("Hello word!!!")

print(f"ขนาดไฟล์ คือ {make_file.stat().st_size}")

content_test = make_file/"test.txt"
content = make_file.read_text()
print(content)