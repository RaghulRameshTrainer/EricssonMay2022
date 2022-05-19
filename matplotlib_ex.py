import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,1],'r',linewidth=3,label="2021-Data")
plt.plot([4,5,1],[1,2,3],'b',linewidth=3,label="2022-Data")
plt.xlabel('Weight')
plt.ylabel('Rupees')
plt.title('Price-Chart')
plt.legend()
plt.show()