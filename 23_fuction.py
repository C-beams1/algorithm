def calculatate_BMI(weight,height):
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"您的BMI分类为：{category}")
    return BMI

result = calculatate_BMI(64,1.755)
print(result)
