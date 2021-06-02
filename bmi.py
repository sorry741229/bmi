h = input('請輸入身高cm: ') # h = height 身高
w = input('請輸入體重kg: ') # w = weight 體重
h = float(h)
w = float(w)
bmi = w  / (( h / 100 )*( h / 100 ))
bmi = int(bmi)
if bmi >= 18.5 and bmi < 24:
    print('你的BMI值為', bmi ,',你的體重為[正常範圍]')
elif bmi >= 24 and bmi < 27:
    print('你的BMI值為', bmi ,',你的體重為[過重]')
elif bmi >= 27 and bmi < 30:
    print('你的BMI值為', bmi ,',你的體重為[輕度肥胖]')
elif bmi >= 30 and bmi < 35:
    print('你的BMI值為', bmi ,',你的體重為[中度肥胖]')
elif bmi >= 35:
    print('你的BMI值為', bmi ,',你的體重為[過度肥胖]')
else:
    print('你的BMI值為', bmi ,',你的體重為[過輕]')