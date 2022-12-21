all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    stydent_dict = {}
    for key in all_array:
        stydent_dict[key] = True
        # 아무값이나 넣어도 상관없음, 키를 이용해서 저장하고 삭제하는 것이기 때문에에
    for key in present_array:
        del stydent_dict[key] # 출석한 학생들 하나하나 제거하기

    for key in stydent_dict.keys():
        return key
        # key 중에 하나를 바로 반환


print(get_absent_student(all_students, present_students)) # 지효
