#plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Positive : 
ax.scatter(low_prob_positive[0],low_prob_positive[1],low_prob_positive[2], alpha=0.05, s=2,color='lightsteelblue')
ax.scatter(middle_prob_positive[0],middle_prob_positive[1],middle_prob_positive[2], alpha=0.05, s=2,color='blue')
ax.scatter(high_prob_positive[0],high_prob_positive[1],high_prob_positive[2], alpha=0.05, s=2,color='midnightblue')

#Negative : 
ax.scatter(low_prob_negative[0],low_prob_negative[1],low_prob_negative[2], alpha=0.05, s=2,color='lightsteelblue')
ax.scatter(middle_prob_negative[0],middle_prob_negative[1],middle_prob_negative[2], alpha=0.05, s=2,color='blue')
ax.scatter(high_prob_negative[0],high_prob_negative[1],high_prob_negative[2], alpha=0.05, s=2,color='midnightblue')

