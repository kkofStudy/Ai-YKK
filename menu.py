def option1():
    print("执行选项 1")

def option2():
    print("执行选项 2")

def option3():
    print("执行选项 3")

def show_menu():
    while True:
        print("\n菜单：")
        print("1. 选项 1")
        print("2. 选项 2")
        print("3. 选项 3")
        print("4. 退出")
        
        choice = input("请输入选项（1-4）：")
        
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("退出程序")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    show_menu()