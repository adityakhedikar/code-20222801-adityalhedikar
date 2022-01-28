
import pandas as pd

mystr = """[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
"""

table1=pd.read_json(mystr)

table1['BMI'] = pd.eval('table1.WeightKg/((table1.HeightCm/100)*(table1.HeightCm/100))')



def BMI_CAT(df):
    
    if (df['BMI'] <= 18.4):
        return 'Underweight'
    elif (18.4 < df['BMI'] <=24.9):
        return 'Normal'
    elif (24.9 < df['BMI'] <=29.9):
        return 'Overweight'
    elif (29.9 < df['BMI'] <= 34.9):
        return 'Moderately obese'
    elif (34.9 < df['BMI'] <= 39.9):
        return 'Severely obese'
    elif (df['BMI'] > 39.9):
        return 'Very Severely obese'
    
table1['BMI_Category'] = table1.apply(BMI_CAT, axis = 1)


def Health_Risk(df):
    
    if (df['BMI'] <= 18.4):
        return 'Malnutrition risk'
    elif (18.4 < df['BMI'] <=24.9):
        return 'Low risk'
    elif (24.9 < df['BMI'] <=29.9):
        return 'Enhanced risk'
    elif (29.9 < df['BMI'] <= 34.9):
        return 'Medium risk'
    elif (34.9 < df['BMI'] <= 39.9):
        return 'High risk'
    elif (df['BMI'] > 39.9):
        return 'Very High risk'
    
table1['Health_Risk'] = table1.apply(Health_Risk, axis = 1)


print('# Overweight Candidates : ' + str(table1[table1.BMI_Category =='Overweight'].count()['BMI_Category']))
