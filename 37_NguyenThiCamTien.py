# STT_HoVaTen.py
# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1:
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh  vien <ten> thanh cong."
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh  vien {name} thanh cong.")

def print_student_list():
    """
    YÊU CẦU 2:
    (Giữ pass ở lần 1 — sẽ hoàn thiện ở feature/print-list)
    """
    print("In danh sách sinh viên thành công!")  # test commit


def search_student(search_name):
    """
    YÊU CẦU 3:
    (Giữ pass ở lần 1 — sẽ hoàn thiện ở feature/search-student)
    """
    pass

# --- Phần thực thi chính để kiểm tra ---
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")

    # Yêu cầu 1: Thêm sinh viên
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    # Phần in & tìm sẽ được hoàn thiện ở các bước sau
    print("\n2. In danh sach sinh vien:")
    print_student_list()

    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")
