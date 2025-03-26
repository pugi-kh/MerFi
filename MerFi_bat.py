print("\"Start MerFi!\"")
print("producer : kihoonkwon")
print("email : jhgfjhgfjhgf96@gmail.com")
print("blog : https://somewhere-in-my-memory.tistory.com/")
print() # 줄바꿈



print("-" * 35)
print("입력하실 폴더명을 포함하는 파일을 \n해당 폴더로 이동합니다.")
print("(!!! 대소문자 주의 !!!)")
print("-" * 35)

# 사용자 입력부
user_confirm = 1
while user_confirm:

    folder_set = set((input("\n======= 폴더명 입력 =======\n(여러개 입력시 '/'로 구분)\n\n>> ")).split('/'))
    folder_list = []
    for fol in folder_set:
        if fol.strip():
            folder_list.append(fol.strip())

    ext = input("\n===== 확장자명 =====\n(모든파일은 Enter)\n\n>> ")

    #%% 폴더명 확인 및 사용자 승인
    folser_list = folder_list.sort()
    list_str = " / ".join(folder_list)
    print()
    print("-"*len(list_str))
    print(list_str)
    print("-"*len(list_str))

    print("\n이대로 진행하시려면 \"Enter\"\n다시 입력하려면 아무 키나 입력해주세요")
    user_confirm = input("\n>> ")

# 파일 생성부

f = open("MerFi.bat", 'w', encoding = "ANSI")

f.write("@Echo off\n")

for s in folder_list:
    f.write(f"mkdir \"{s}\"\n")
    f.write(f"move *\"{s}\"*\"{ext}\" \"{s}\"\n")
    f.write(f"rmdir \"{s}\"\n")

f.close()

print("\n=================================\n")
print("파일 생성이 완료되었습니다.\n")
print("\"MerFi.bat\" 파일을 \n정리할 폴더 내에서 실행하면 \n파일 정리가 진행됩니다.")
print("\n감사합니다.")
print("\n=================================")
print("\n" * 10)
input()