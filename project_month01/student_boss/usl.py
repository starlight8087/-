"""
    界面逻辑层
"""

from bll import StudentManagerController
from model import StudentModel

class StudentManagerView:
    """
        学生管理器视图,负责处理界面逻辑.
    """
    def __init__(self):
        self.__controller = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")

    def __select_menu_item(self):
        item = input("请您输入选项:")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def get_int_info(self,str_info):
        while True:
            try:
                result = int(input("请输入%s:"%str_info))
                return result
            except:
                print("%s输入有误"%str_info)

    def __input_students(self):
        # 调用逻辑控制类的add_student方法
        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名:")
            if stu.name == "":
                break
            stu.age = self.get_int_info("年龄")
            stu.score = self.get_int_info("成绩")
            # while True:
            #     try:
            #         stu.score = int(input("请输入成绩:"))
            #         break
            #     except:
            #         print("年龄输入有误")
            self.__controller.add_student(stu)



    def __output_students(self):
        for item in self.__controller.stu_list:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        while True:
            # id = int(input("请输入需要删除的学生编号:"))
            id = self.get_int_info("需要删除的学生编号")
            if self.__controller.remove_student(id):
                print("删除成功")
                break
            else:
                print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入新的姓名:")
        stu.age = int(input("请输入新的年龄:"))
        stu.score = int(input("请输入新的成绩:"))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")