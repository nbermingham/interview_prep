import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# give 0/1 labels denoting postives and negatives
labels = np.array([np.ones(50), np.zeros(50)]).reshape(100)
# generate the random values from two separate gaussian distributions
values = np.round(np.array([np.random.normal(150, 30, 50), np.random.normal(100, 30, 50)])).reshape(100)
change_num = int(np.random.rand()) + 1
# indices that will be "accidentally" multiplied by 100
int_changes = np.random.choice(100, change_num, replace=False)
values2 = np.copy(values)
# multiplies the second array by 100 at the given indices
for change in int_changes:
    values2[change] *= 100

fig, ax = plt.subplots(1,2, figsize=(16,6))
ax1, ax2 = ax[0], ax[1]
sns.regplot(x=values, y=labels, logistic=True, ci=False, ax=ax1, label="Error free model")
sns.regplot(values2, labels, logistic=True, ci=False, ax=ax1, label="Model with errors")
ax1.set_xscale("log")
ax1.legend(loc=9)
ax1.set_title("Logistic regressions")
sns.displot(values2, kde=False, bins=[1*10**(i/10) for i in range(51)], ax=ax2)
ax2.set_xscale("log")
ax2.set_title("Histogram of variable")
plt.show()
