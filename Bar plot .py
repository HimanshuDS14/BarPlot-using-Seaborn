import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("tips.csv")
print(data.head())

x = data["day"]
y = data["tip"]
z = data["sex"]

sns.barplot(x = x , y =y , data = data)

plt.show()

sns.barplot(x = x , y = data["total_bill"] , data = data)
plt.show()



sns.barplot(x = x ,y = y , data = data , hue = data["sex"])
plt.show()


sns.barplot(x = data["total_bill"] , y = data["day"] , data = data)
plt.title("Horizontal barplot")
plt.show()

sns.barplot(x = data["total_bill"] ,y = data["day"] , data = data , order=["Sun" ,"Mon"  , "Thur"] , color="green")
plt.title("Plot only sunday and monday")
plt.show()