#
# year = "兔"
# name = "小明"
# message_cotent = """
# 金{0}贺岁，欢乐祥瑞。
# 金{0}敲门，五福临门。
# 给{1}及家人拜年啦！
# 新春快乐，{0}年大吉！
# """.format(year,name)
# print(message_cotent)
#
# year = "兔"
# name = "小明"
# message_cotent = """
# 金{current_year}贺岁，欢乐祥瑞。
# 金{current_year}敲门，五福临门。
# 给{receiver_name}及家人拜年啦！
# 新春快乐，{current_year}年大吉！
# """.format(current_year = year,receiver_name = name)
# print(message_cotent)
#
# year = "兔"
# name = "小明"
# message_cotent = f"""
# 金{year}贺岁，欢乐祥瑞。
# 金{year}敲门，五福临门。
# 给{name}及家人拜年啦！
# 新春快乐，{year}年大吉！
# """
# print(message_cotent)
#
gpa_dict = {"小明":3.214,"小红":3.222,"小张":3.914,"小林":3.814,}
for name,gpa in gpa_dict.items():
    print("{0}你好，你的当前绩点为：{1:.2f}".format(name,gpa))