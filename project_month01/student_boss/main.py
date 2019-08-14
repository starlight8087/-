"""
    程序入口
"""
from usl import StudentManagerView

# 如果是主模块 才运行
# 如果从别的模块把我导入,我可不干活啊.
if __name__ == "__main__":
    # try:
    view = StudentManagerView()#
    view.main()
# except:
#     print("出错啦")