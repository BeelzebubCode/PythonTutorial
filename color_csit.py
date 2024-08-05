import os

def print_orange(text):
    # ANSI escape code สำหรับสีส้ม
    ORANGE_COLOR_CODE = '\033[38;5;208m'
    RESET_COLOR_CODE = '\033[0m'
    
    # การปริ้นท์ข้อความที่มีสีส้ม
    print(f"{ORANGE_COLOR_CODE}{text}{RESET_COLOR_CODE}")

# ข้อความ ASCII Art
ascii_art = """
░█████╗░░██████╗██╗████████╗
██╔══██╗██╔════╝██║╚══██╔══╝
██║░░╚═╝╚█████╗░██║░░░██║░░░
██║░░██╗░╚═══██╗██║░░░██║░░░
╚█████╔╝██████╔╝██║░░░██║░░░
░╚════╝░╚═════╝░╚═╝░░░╚═╝░░░
"""

# การเรียกใช้ฟังก์ชันเพื่อแสดง ASCII Art ในสีส้ม
os.system("cls")
print_orange(ascii_art)
while True:
    a = 10
