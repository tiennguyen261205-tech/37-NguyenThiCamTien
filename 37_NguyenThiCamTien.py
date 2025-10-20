def search_student(search_name):
    print("--- KET QUA TIM KIEM ---")
    found = False
    for student in student_list:
        if search_name.lower() in student["name"].lower():
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")
            found = True
    if not found:
        print("Khong tim thay sinh vien nao.")
