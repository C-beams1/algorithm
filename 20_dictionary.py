# 结合input、字典、if判断，做一个查询流行语含义的电子词典程序
slang_dict = {"一":"觉醒年代" ,
             "二":"YYDS"}
slang_dict["三"] = "双减"
slang_dict["四"] = "破防"
slang_dict["五"] = "元宇宙"

query = input("请输入你想要查询的流行语号：")
if query in slang_dict:
    print("您查询的" + query + "含义如下")
    print(slang_dict[query])
else:
    print("您查询的流行语暂未收入。")
    print("当前的词典收录的词条数为：" + str(len(slang_dict)) + "条。")