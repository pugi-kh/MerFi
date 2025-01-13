# ** MerFi -> Merge Files
'''
Revit을 사용하는 건축설계사무소에서 근무하면서
협력사와 작업할 때
도면을 cad file로 내보내는 경우가 많았는데,
Revit에서는 평면도, 입면도 이런식으로 도면별로 cad file을 하나로 묶어서 추출이 불가능하고,
평면도_1층.dwg, 평면도_2층.dwg,...,입면도_정면.dwg, 입면도_우측면.dwg,... 이런 형태로 
모두 낱장으로 출력하고 폴더로 분리한 뒤 파일을 합치는 작업을 했었다.

이때, 유사한 이름을 가진 파일들을 자동으로 묶어서 
폴더별로 정리해주는 프로그램이 있었으면 좋겠다는 생각이 들어,
이 프로그램을 만들어보고자 하게 되었다.


** 입력받을 변수
폴더의 경로 : user_path
시작자리, 끝자리 번호 : start_num, last_num
확장자명 : file_extension



** 작동방식

- 사용자로부터 정리할 파일들이 있는 폴더의 경로를 입력받는다. | 경로 변수명 : user_path
- 경로 내에 있는 파일들의 이름을 리스트화 한다. | 리스트명 : file_set

- 해당 파일들 이름의 몇번째 자리부터 몇번째 자리까지 동일한 파일들을 묶을 것인지
  시작하는 자리의 번호와, 끝나는 자리의 번호를 입력받는다. | 변수명 : start_num, last_num
- 이때 설정한 번호가 맞는지 예시로 생성될 폴더명 하나를 보여주어 사용자가 확인할 수 있도록 한다.

- 입력받은 번호를 인덱스번호로 변환해 리스트 내의 요소들을 각각 슬라이싱해 집합을 만들어
  중복요소가 제거된 컬렉션을 만든다. | 변수명 : folder_set
ex) 파일명 : 20250109_평면도_1층.dwg -> start_num = 10 , last_num = 12 
-> 폴더명 : "평면도"

- 터미널이 입력받은 user_path에서 동작하도록 현재 위치를 변경
- 현재 위치에 folder_set의 요소의 이름과 동일한 폴더들을 생성한다.
- 폴더명을 "평면도"라고 가정했을 때, 여기에 들어갈 파일명은 "*평면도*"로 표현할 수 있다.
- 특정 확장자만 이동하고자 하면, 사용자로부터 확장자명을 입력받는다. | 변수명 : file_extension
- 만약 확장자를 ".dwg"라고 입력했다면 옮겨질 파일명은 "*평면도*.dwg"라고 볼 수 있다.

- mkdir, move 등을 이용해 폴더를 생성하고 파일을 이동한다.



** 기존파일 참고
기존에 .bat 파일로 만들어 놨던 것을 참고하자면,

mkdir "AXG"
mkdir "AFP"
mkdir "APT"
...
move *"AXG"*"" "AXG"
move *"AFP"*"" "AFP"
move *"APT"*"" "APT"
...
rmdir "AXG"
rmdir "AFP"
rmdir "APT"
...


위와 같이 작성했엇다.

이때, rmdir을 사용한 이유는 그때그때 이동할 파일명을 설정한 것이 아니라, 
초기 설정을 해놓고 사용하면서, 만약 파일이 없으면 필요없는 폴더를 지우기 위해서 작성한 것이다.
지금은 move까지만 작성하면 될것으로 판단된다.

여기에서 (move *AXG* AXG)와 (move *"AXG"*"" "AXG")는 동일하게 작동하지만,
띄어쓰기 등이 파일명에 속해있을 가능성이 있어
이것이 파일 실행에 영향을 줄 수 있기 때문에 안전하게 따옴표로 묶는 방식을 택했다.
'''
#======================================================================
import os
import shutil
import time

print("\"Start MerFi!\"")
print("ver.1.00.3")
print("producer : kihoonkwon")
print("email : jhgfjhgfjhgf96@gmail.com")
print("blog : https://somewhere-in-my-memory.tistory.com/")
print() # 줄바꿈
#%% 사용자로부터 입력받기기
print("정리할 파일들이 있는 폴더의 경로를 입력해주세요")
user_path = input(r"폴더 경로 : ")
user_confirm = '3'

while True:
    if user_confirm != '3':
        break
    else:
        print("\n파일명 \"몇번째 자리부터\" \"몇번째 자리까지\" \n이름이 동일한 파일을 폴더별로 정리할까요?\n")
        start_num = int(input("몇번째 자리부터 : "))
        end_num = int(input("몇번째 자리까지 : "))
        print("==========================================")
        print("이후 작성시에는 대소문자를 잘 확인해주세요.")
        print("==========================================")
        extention = input("확장자명(모든파일은 Enter!) : ")

        #%% 역슬래시를 슬래시로 변경해서 출력
        user_path = user_path.replace('\\','/')
        #====================================================
        print(user_path)

        #%% 경로 내 파일명 리스트화화
        file_set = os.listdir(user_path)
        # print(file_set)

        folder_set = set() # 폴더명을 세트로 만들어서 중복제거
        file_list = []

        for a_file in file_set: # 파일명 하나씩 출력
            if a_file.endswith(extention): # 파일 확장자가 입력과 동일한 경우
                file_list.append(a_file) # 확장자가 동일한 파일이름은 리스트에 추가

                a_folder = a_file[start_num - 1:end_num] # 파일명에서 중복된 영역이 폴더명
                if a_folder == "": # 빈 파일명은 추가하지 않음
                    pass
                else: # 비어있지 않다면 폴더명리스트에 추가
                    folder_set.add(a_folder)
                
        #%% 폴더 리스트 CRUD
        folder_list = list(folder_set)
        folder_list.sort()  # 사용자가 확인하기 쉽도록 리스트 정렬

        print(f"\n{folder_list}\n")
        print("위 목록대로 폴더를 생성합니다.\n")
        time.sleep(0.5)
        print("0. 확인완료(작업진행)\n1. 추가\n2. 삭제\n3. 다시 입력")
        user_confirm = input("\n입력 : ")
    

#=========================================================================
#=========================================================================
#=========================================================================
# 여기 작업중 : 폴더명 한번에 여러개 추가 제거

folder_set2 = set() # 추가, 제거를 위한 폴더명 집합 사용

while True:
    # 사용자가 확인 할 때까지 세트 요소 수정
    if user_confirm == '0':
        break
    
    elif user_confirm == '1':
        a_folder = input("추가할 파일명 : ")
        if len(a_folder) == 0:
            pass
        else :
            folder_set.add(a_folder)

    elif user_confirm == '2':
        a_folder = input("삭제할 파일명 : ")
        folder_set2 = set(a_folder)
        folder_set2 = folder_set2 - {',', ' '}
        folder_set.union(folder_set2)

    else:
        print("0, 1, 2 중에서 선택해주세요")
        time.sleep(0.5)
    
    folder_list = list(folder_set)
    folder_list.sort()
    
    print(f"\n{folder_list}\n")
    print("위 목록대로 폴더를 생성합니다.\n")
    time.sleep(0.5)
    print("0. 확인완료(작업진행)\n1. 추가\n2. 삭제")
    user_confirm = input("\n입력 : ")
    
    # 폴더명 추가 혹은 삭제시, 대소문자를 구문해서 작성해야 하며
    # 프로그램이 원활히 동작하지 않을 수 있음.

print("\n파일 정리를 시작합니다...잠시만 기다려 주세요...\n")
# 여기까지 폴더명 정리 완료
# 해당 폴더명과 파일명이 겹치는 경우 파일을 해당 폴더로 이동해야 함.
#%% 파일 이동 함수 작성 (재귀함수 활용)

        
#%% 파일 이동 MoveFiles 함수 적용
for i in range(len(folder_list)): # 폴더 개수만큼 수행
    # os.mkdir(user_path + folder_list[i]) # 옮길 폴더 생성
    # 폴더가 기존에 있는지 확인하고 있으면 건너뛰기
    if not os.path.exists(user_path + folder_list[i]):
        os.makedirs(user_path + folder_list[i])
    
    # 파일중에서 이름이 겹치긴 하는데 위치가 다른 경우 제외
    li = [s for s in file_list if folder_list[i] in s and folder_list[i] == s[start_num - 1 : end_num]] # 옮길 파일 리스트
    li.sort()
    
    
    while True: 
        current_path = (user_path + li[0])
        new_path = (user_path + folder_list[i] + '/' + li[0])
        if len(li) < 2:
            shutil.move(current_path, new_path)
            break
        shutil.move(current_path, new_path)
        li = li[1:]

print("정리가 완료되었습니다. 감사합니다.")
time.sleep(3)