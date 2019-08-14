"""
    数据模型
"""
class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0):
        """
            创建学生对象
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = None
        self.name = name
        self.age = age
        self.score = score