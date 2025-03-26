# ** MerFi -> Merge Files
print("\"Start MerFi!\"")
print("producer : kihoonkwon")
print("email : jhgfjhgfjhgf96@gmail.com")
print("blog : https://somewhere-in-my-memory.tistory.com/")
print() # 줄바꿈






#%% start!
import os
import shutil
import time


print("~ 정리할 파일들이 있는 폴더의 경로를 입력해주세요 ~")
user_path = input(r">> ")
extention = input("\n~ 확장자명 ~\n(모든파일은 Enter!)\n>> ")

# 폴더 경로를 파이썬에서 사용 가능하도록 정리
user_path = user_path.replace('\\','/') + '/'
user_path = user_path.replace('//', '/')


# 파일 리스트화
file_list = os.listdir(user_path)

# 확장자가 입력과 다른 경우 제거
for a_file in file_list:
    if not a_file.endswith(extention): 
        file_list.remove(a_file)


# 이후 범위를 지정할 것인지, 폴더명을 입력할 것인지 확인
print("\n~ 중복되는 파일명을 폴더로 생성합니다. ~")
print("  1. 범위를 지정하여 폴더명 추출")
print("  2. 직접 중복되는 문자 입력해서 폴더명 생성")
user_confirm = input(">> ")


folder_set = set() # 폴더명을 세트로 만들어서 중복제거
folder_temp = set() # 추가, 제거거를 위한 폴더명 집합 사용 -> 함수 적용 후에는 삭제
#%% 사용자가 확인 할 때까지 세트 요소 수정
while True:
# 메뉴 1) 사용자로부터 입력받기기
    if user_confirm == '1':

        folder_set = set() # 폴더세트 초기화
        while True:
            print("\n~ 파일명에서 \"몇번째 자리부터\" \"몇번째 자리까지\" 폴더명으로 지정할까요? ~\n")
            # 하나의 파일을 가져와서 자리수 확인 -> 위 리스트에서?
            # 사용자가 파일명 입력하고 자리수 확인해도 좋을 듯 -> 직접 추가로 입력
            start_num = input("몇번째 자리부터 (모르겠으면 Enter)\n>> ")
            if not start_num:
                for_check = input("자리수 확인할 파일명 붙여넣기\n>> ")
                for i in range(len(for_check)):
                    print(f"    {for_check[i]} \t:  ", end ="")
                    print(str(i+1).zfill(2), end = "\n")
                continue # 여기에 파일명 입력하고 범위번호 확인하는 부분분
            else: 
                end_num = int(input("몇번째 자리까지\n>> "))
                start_num = int(start_num)
                break


        for a_file in file_list: # 파일명 하나씩 출력
            a_folder = a_file[start_num - 1:end_num] # 파일명에서 중복된 영역이 폴더명
            a_folder = a_folder.strip()
            if a_folder: # 빈 값이 아니라면 폴더명 세트에 추가
                folder_set.add(a_folder)

# 메뉴 2) 폴더명 추가 부분
    if user_confirm == '2':

        print("~ 추가할 ", end = "")
        #=========================================================================
        # 함수로 만들어서 적용
        print("파일명 입력 ~")
        print("(여러개의 경우 \"/\"슬래시로 구분)")
        print("(대소문자 주의)")
        a_folder = input(">> ")
        folder_list = a_folder.split('/')

        # folder_temp = set()

        for i in range(len(folder_list)): # folder_list 서식 맞추기, 정리
            # 폴더명 작성시 잘못 작성된 부분 삭제
            if len(folder_list[i]) > 0 : 
                folder_list[i] = folder_list[i].strip()
                folder_temp.add(folder_list[i])
        # return folder_temp
        #=========================================================================
        
        folder_set = folder_set.union(folder_temp)
        folder_temp = set() # 임시세트 초기화 -> 함수 적용 후에는 삭제

# 메뉴 3) 폴더명 삭제 부분
    if user_confirm == '3':

        a_folder = input("삭제할 ", end = "")
        #=========================================================================
        # 함수로 만들어서 적용
        print("파일명 입력 ~")
        print("(여러개의 경우 \"/\"슬래시로 구분)")
        print("(대소문자 주의)")
        a_folder = input(">> ")
        folder_list = a_folder.split('/')

        # folder_temp = set()

        for i in range(len(folder_list)): # folder_list 서식 맞추기, 정리
            # 폴더명 작성시 잘못 작성된 부분 삭제
            if len(folder_list[i]) > 0 : 
                folder_list[i] = folder_list[i].strip()
                folder_temp.add(folder_list[i])
        # return folder_temp
        #=========================================================================
        
        folder_set = folder_set - folder_temp
        folder_temp = set() # 임시세트 초기화 -> 함수 적용 후에는 삭제

# 번호 잘못 입력
    if user_confirm not in {'0', '1', '2', '3'}:

        print("다시 입력해주세요")
        time.sleep(0.5)
        user_confirm = input(">> ")

# 폴더 리스트 출력, 사용자 확인인
    elif user_confirm in {'1', '2', '3'}:

        folder_list = list(folder_set)
        folder_list.sort()
        # 생성된 폴더명 출력
        '''
        #======================================
        # for i in range(len(folder_list)):
        #     print(folder_list[i], end = "")
        #     if i < len(folder_list) - 1 :
        #         print(" / ", end = "")
        #======================================
        # .join을 활용해서 리스트를 " / "로 연결해서 출력하면 되는구나..
        '''
        print()
        print(" / ".join(folder_list))
        print()

        print("위 목록대로 폴더를 생성합니다.\n")
        time.sleep(0.5)
        print("0. 확인완료(작업진행)\n1. 범위 다시지정\n2. 추가\n3. 삭제")
        user_confirm = input("\n>> ")

    # 폴더명 추가 혹은 삭제시, 대소문자를 구문해서 작성해야 하며
    # 프로그램이 원활히 동작하지 않을 수 있음.
# 사용자 확인시 다음 작업 진행행
    else : # user_confirm == '0':
        break
print("\n파일 정리를 시작합니다...잠시만 기다려 주세요...\n")
# 여기까지 폴더명 정리 완료
# 해당 폴더명과 파일명이 겹치는 경우 파일을 해당 폴더로 이동해야 함.


#%% 파일 이동
for i in range(len(folder_list)): # 폴더 개수만큼 수행
    # os.mkdir(user_path + folder_list[i]) # 옮길 폴더 생성
    if not os.path.exists(user_path + folder_list[i]): # 생성하려는 폴더명이 기존에 없을 경우
        os.makedirs(user_path + folder_list[i]) # 폴더 생성
    
    #============================================================
    # 파일중에서 이름이 겹치긴 하는데 위치가 다른 경우 제외?
    # 이부분 어떻게 할지 고민
    # li = [s for s in file_list if folder_list[i] in s and folder_list[i] == s[start_num - 1 : end_num]] 
    li = [s for s in file_list if folder_list[i] in s] 
    # 문자를 포함하기만 하면
    li.sort() # 문자를 포함하는 리스트를 만든 후
    
    # 튜플 등으로 한번에 이동이 가능한지 확인 하면 좋지 않을까
    for fname in li:
        current_path = (user_path + fname) # 리스트의 첫번째 파일 현재 주소
        new_path = (user_path + folder_list[i] + '/' + fname) # 이동할 파일의 주소
        shutil.move(current_path, new_path)
    
    # while True: 
    #     current_path = (user_path + li[0]) # 리스트의 첫번째 파일 현재 주소
    #     new_path = (user_path + folder_list[i] + '/' + li[0]) # 이동할 파일의 주소
    #     if len(li) < 2:
    #         shutil.move(current_path, new_path)
    #         break
    #     shutil.move(current_path, new_path)
    #     li = li[1:]
# 2개의 폴더명을 모두 포함하는 파일이 있으면 오류가 나지 않을까?
    file_list = [x for x in file_list if x not in li] # 이동한 파일은 리스트에서 제외외

print("정리가 완료되었습니다. 감사합니다.")
time.sleep(3)