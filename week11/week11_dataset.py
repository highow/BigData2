import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 성별에 따른 생존율 계산
titanic = sns.load_dataset('titanic')
# print(titanic['sex'].head())
# print(titanic.info())
gender_survival = titanic.groupby(by='sex')['survived'].mean()
print(gender_survival)



# titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
# titanic['deck'].fillna('Unknown', inplace=True)
# print(titanic['deck'])
# print(titanic.info())

# print(titanic['survived'])
# print(titanic.info())

# 생존자 수와 사망자 수 시각화
# sns.countplot(data=titanic, x='survived')
# plt.title('Survived (0 = No, 1 = Yes)')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()