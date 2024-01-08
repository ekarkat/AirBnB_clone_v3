from flask import Flask, abort, request

app = Flask(__name__)

ar1 = 15

def numbers(a, b):
    print(a, b)


# class Num:
#     a = 0
#     b = 0
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# a1 = Num(15, 17)
# a2 = Num(18, 13)
# a3 = Num(20, 18)
# a4 = Num(2, 24)
# a5 = Num(5, 77)
# a6 = Num(1, 87)

# i = 1

# a_list = [a1, a2, a3, a4, a5, a6]

# dic = {}

# for a in a_list:
#     dic["a{}".format(i)]=a
#     i += 1

# sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1].a))

# # print(type(dic.items()))

# for item in dic.items():
#     print(item)