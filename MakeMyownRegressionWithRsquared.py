from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6],dtype=np.float64)
ys = np.array([4,6,4,5,8,10],dtype=np.float64)

#plt.scatter(xs,ys)
#plt.show()
#m= mean xs*mean ys - mean xs*ys / mean xs * mean xs - mean x**2 
def best_fit_slope(xs,ys):
    m=(((mean(xs)*mean(ys)) - mean(xs*ys))/
      ((mean(xs)*mean(xs))- mean(xs**2)))
    b = mean(ys) - m*mean(xs)
    return m, b
def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)
def coefficient_of_dermination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig)for y in ys_orig]
    squared_error_regr = squared_error(ys_orig,ys_line)
    squared_error_y_mean = squared_error(ys_orig,y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)
m,b = best_fit_slope(xs,ys)

print(m,b)

regression_line = [(m*x)+b for x in xs]

predict_x = 10
predict_y =(m*predict_x)+b
r_squared = coefficient_of_dermination(ys,regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y)
plt.plot(xs,regression_line)
plt.show()
