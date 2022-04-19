import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

labels = np.array([np.ones(50), np.zeros(50)]).reshape(100)
values = np.round(np.array([np.random.normal(150, 30, 50), np.random.normal(100, 30, 50)])).reshape(100)

print("hello world")