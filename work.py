# 学习sql
# 安装navicat  库pymysql
# 自学导包 import XXX      from XXXX import XXX    import XXX as YYY
# import pymysql   并学习库的使用
# 改项目 利用pymysql
# pass
pass

info_dict = {
    "张三": {
        '学号': 1, '年龄': 18
    },
    "李四": {
        '学号': 2, '年龄': 19
    },
    "王五": {
        '学号': 3, '年龄': 20
    },
}


def print_menu():
    print("*" * 20)
    print("系统功能菜单")
    print("*" * 20)
    print("1. 展示所有学生信息")
    print("2. 增加学生信息")
    print("3. 删除学生信息")
    print("4. 修改学生信息")
    print("5. 查询学生信息")
    print("6. 退出系统")
    print("*" * 20)


def show_info():
    print("姓名****** 学号 ******年龄")
    for it in info_dict.items():
        name = it[0]
        id = it[1]["学号"]
        age = it[1]["年龄"]
        print(name, "*" * 6, id, "*" * 6, age)
    pass


def insert_stu_info():
    name = input("请输入学生姓名：")
    id = int(input("请输入学生学号："))
    age = int(input("请输入学生年龄："))
    info_dict[name] = {"学号": id, "年龄": age}


def delete_stu_info(name):
    if not search_stu_info(name):

        return
    name = input('请输入要删除的学生姓名')
    del info_dict['name']
    pass


def modify_stu_info(name):
    # 判断该学生是否存在
    if not search_stu_info(name):
        print("该学生不存在！！！")
        return

    id = input("请修改学生的ID:")
    age = input("请修改学生的age:")

    info_dict[name] = {"学号": id, "年龄": age}


def search_stu_info(name):
    # info_dict[name] =[]   hash_tab
    for it in info_dict.items():
        if it[0] == name:
            print(name, "*" * 6, it[1]["学号"], "*" * 6, it[1]["年龄"])
            return True

    print("该学生不存在！！！")
    return False


def func(fun_id):
    if fun_id == 1:
        show_info()
    elif fun_id == 2:
        insert_stu_info()
    elif fun_id == 3:
        name = input("请输入删除的学生姓名：")
        delete_stu_info(name)
    elif fun_id == 4:
        name = input("请输入修改的学生姓名：")
        modify_stu_info(name)
    elif fun_id == 5:
        name = input("请输入查询的学生姓名：")
        search_stu_info(name)
    elif fun_id == 6:
        return None
    else:
        print("没有此功能")


pass


def main():
    # 打印功能表
    print_menu()

    while True:
        fun_id = int(input("请输入您要执行的功能："))
        # func(fun_id)

        if func(fun_id) == None:
            break



if __name__ == '__main__':
    main()
