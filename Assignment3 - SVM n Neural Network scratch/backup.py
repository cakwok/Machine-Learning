#Q1.4 plotting margin and SVM
#plot margin by 1 dimension, plotting x2 instead of meshgrid
x2_positive_margin = 1/weight[1] -w0/weight[1] - weight[0]/weight[1] * x1_coord
x2_negative_margin = -1/weight[1] -w0/weight[1] - weight[0]/weight[1] * x1_coord
plt.plot(x1_coord, x2_positive_margin, color='blue')
plt.plot(x1_coord, x2_negative_margin, color='red')
