"""
    业务逻辑层
"""
class StudentManagerController:
    """
        学生管理控制器,负责处理对学生列表的逻辑操作.
    """

    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_target):
        """
            添加学生
        :param stu_target: 需要添加的学生对象
        """
        stu_target.id = self.__generate_id()
        self.__stu_list.append(stu_target)

    def __generate_id(self):
        # 类名.类变量  增加1
        StudentManagerController.__init_id += 1
        # 返回类变量
        return StudentManagerController.__init_id

    def remove_student(self,id):
        """
            移除学生信息
        :param id: int类型,需要移除的学生编号
        :return: 是否移除成功True表示成功,False表达失败
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self,stu_target):
        """
            修改学生信息
        :param stu_target: 学生类型对象,id是需要修改的学生编号
                            其他信息是新的数据.
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_target.id:
                item.name = stu_target.name
                item.age = stu_target.age
                item.score = stu_target.score
                return True
        return False