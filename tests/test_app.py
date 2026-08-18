from app import search_students

def test_search_student_found():
    # Trường hợp 1: Tìm thấy sinh viên
    result = search_students("Nguyen")
    assert len(result) > 0
    assert result[0]["name"] == "Nguyen Van A"

def test_search_student_not_found():
    # Trường hợp 2: Không tìm thấy sinh viên
    result = search_students("Xyz")
    assert len(result) == 0

def test_search_student_case_insensitive():
    # Trường hợp 3: Tìm kiếm không phân biệt hoa/thường
    result_lower = search_students("nguyen")
    result_upper = search_students("NGUYEN")
    assert len(result_lower) > 0
    assert len(result_lower) == len(result_upper)
