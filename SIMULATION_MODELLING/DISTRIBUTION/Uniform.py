# import uniform distribution
from scipy.stats import uniform
# import matplotlib
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})

# random numbers from uniform distribution
n = 10000
start = 1
width = 20
data_uniform = uniform.rvs(size=n, loc=start, scale=width)

# Create a distribution plot
ax = sns.histplot(data_uniform, bins=100, kde=True, color='skyblue', stat='density')
ax.set(xlabel='Uniform Distribution', ylabel='Density')
plt.show()