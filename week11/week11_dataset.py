from pydoc import describe

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# print(titanic.info())
# titanic['age'].fillna(titanic['age'].mean(), inplace=True)
# print(titanic.info())
# print(titanic['age'])
# age_survival = titanic.groupby(by='age')['survived'].mean().reset_index()
# sns.barplot(data=age_survival, x='age', y='survived')
# plt.title('Survival Rate by Age')
# plt.xlabel('Age')
# plt.ylabel('Survival Rate')
# plt.show()

median_age = titanic['age'].median()
# mean_age = titanic['age'].mean()
# print(median_age, mean_age)
titanic_fill_row = titanic.fillna({'age' : median_age})
print(titanic_fill_row)
titanic_fill_row['survived'] = titanic_fill_row['survived'].astype(float)
print(titanic_fill_row['age'])
sns.histplot(data=titanic_fill_row, x='age', weights='survived', bins=8, kde=False)
plt.title('Survival Rate by Age (Fill with Median)')
plt.xlabel('Age')
plt.ylabel('Survival Rate (weights)')
plt.show()


# titanic_drop_row = titanic.dropna(subset=['age'])
# print(titanic_drop_row.info())
# titanic_drop_row['survived'] = titanic_drop_row['survived'].astype(float)
# print(titanic_drop_row['survived'])
#
# plt.figure(figsize=(10, 5))
# sns.histplot(data=titanic_drop_row, x='age', weights='survived', bins=8, kde=False)
# plt.title('Survival Rate by Age (Drop NaN rows)')
# plt.xlabel('Age')
# plt.ylabel('Survival Rate (weights)')
# plt.show()

# print(titanic['sex'].head())

# gender_survival = titanic.groupby(by='sex')['survived'].mean()
# print(type(gender_survival))
# gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
# print(gender_survival)
# print(gender_survival.info())
#
# sns.barplot(data=gender_survival, x='sex', y='survived')
# plt.title('Survival Rate by Gender')
# plt.xlabel('Sex')
# plt.ylabel('Survival Rate')
# plt.show()




# titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
# titanic['deck'].fillna('Unknown', inplace=True)
# print(titanic['deck'])
# print(titanic.info())

# print(titanic['survived'])
# print(titanic.info())

# sns.countplot(data=titanic, x='survived')
# plt.title('Survived (0 = No, 1 = Yes)')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()