import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as stat

#CSV format: GENDER, SCREEN, SLEEP

#pandas csv reading function
data=pd.read_csv('sleepscreendata.csv',header=None).values

####INITIALIZING LISTS####

#male lists for sleep and screen time
maleSleep=[]
malePhone=[]
#female lists for sleep and screen time
femaleSleep=[]
femalePhone=[]
#nonbinary lists for sleep and screen time
nbSleep=[]
nbPhone=[]
#other lists for sleep and screen time
otherSleep=[]
otherPhone=[]
malecount = 0
femalecount = 0
nbcount = 0
othercount = 0
#list for collecting the gender data
genData = [x[0] for x in data]


####GETTING GENDER COUNTS####

for u in range(len(genData)):
  if genData[u] == 'male':
    malecount = malecount + 1
  if genData[u] == 'female':
    femalecount = femalecount + 1
  if genData[u] == 'nonbinary':
    nbcount = nbcount + 1
  if genData[u] == 'other':
    othercount = othercount + 1


####SEPERATING CSV DATA####
    
#for loop to get the x coord
for i in range(len(genData)):
  #for loop to get the y coord
  for j in range(3):
    #collecting male data
    if genData[i] == 'male':
      if j == 1:
        malePhone.append(float(data[i][j]))
      elif j == 2:
        maleSleep.append(float(data[i][j]))
    #collecting female data
    elif genData[i] == 'female':
      if j == 1:
        femalePhone.append(float(data[i][j]))
      elif j == 2:
        femaleSleep.append(float(data[i][j]))
    #collecting nonbinary data
    elif genData[i] == 'nonbinary':
      if j == 1:
        nbPhone.append(float(data[i][j]))
      elif j == 2:
        nbSleep.append(float(data[i][j]))
    #collecting other genders data
    elif genData[i] == 'other':
      if j == 1:
        otherPhone.append(float(data[i][j]))
      elif j == 2:
        otherSleep.append(float(data[i][j]))
    else:
      continue


#####PLOTTING#####
#X-AXIS: Screen Time (in hours)
#Y-AXIS: Sleep Time (in hours)
#RED = FEMALE
#BLUE = MALE
#GREEN = NON-BINARY
#GREY = OTHER
plt.figure()
#Male plotting
plt.scatter(malePhone, maleSleep, color = 'blue', marker='o', label="Male")
#Female plotting
plt.scatter(femalePhone, femaleSleep, color = 'red', marker='o', label="Female")
#Non-Binary plotting
plt.scatter(nbPhone, nbSleep, color = 'green', marker='o', label="Non-Binary")
#Other plotting
plt.scatter(otherPhone, otherSleep, color = 'grey', marker='o', label="Other")
#plt.legend(loc="upper right")

#Inverting the X axis
ax = plt.gca()
#ax.set_xlim(ax.get_xlim()[::-1])
ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
ax.set_yticks([0, 2, 4, 6, 8, 10, 12, 14])
ax.grid(which = 'major', color = 'black')
ax.grid(which = 'minor', color = 'black', alpha=0.2)
ax.minorticks_on()




#Titles and axis names
plt.title("Phone Usage and Sleep Scatter")
plt.ylabel("Sleep Time (Hours)")
plt.xlabel("Screen Time (Hours)")




######PRINTING SOME GENERAL STATISTICAL DATA#####
#printing total number of people in a category
print("Total Number of Female Participants: ", femalecount)
print("Total Number of Male Participants: ", malecount)
print("Total Number of Non-Binary Participants: ", nbcount)
print("Total Number of Other Participants: ", othercount)

#making lists of the combined genders info for general information
wholeSleep = femaleSleep + maleSleep + nbSleep + otherSleep
wholePhone = femalePhone + malePhone + nbPhone + otherPhone
#general info
print("Average General Sleep Time: \t", round(stat.mean(wholeSleep), 2))
print("Average General Screen Time: \t", round(stat.mean(wholePhone), 2))
#female info
print("Average Female Sleep Time: \t", round(stat.mean(femaleSleep), 2))
print("Average Female Screen Time: \t", round(stat.mean(femalePhone), 2))
#male info
print("Average Male Sleep Time: \t", round(stat.mean(maleSleep), 2))
print("Average Male Screen Time: \t", round(stat.mean(malePhone), 2))
#nb info
print("Average Non-Binary Sleep Time: \t", round(stat.mean(nbSleep), 2))
print("Average Non-Binary Screen Time: ", round(stat.mean(nbPhone), 2))
#other info
#print("Average other Sleep Time: \t", round(stat.mean(otherSleep), 2))
#print("Average other Screen Time: \t", round(stat.mean(otherPhone), 2))

#Regression Line Calculation

#REGRESSION LINE FUNCTIONS

#Slope function, formula: nΣxy - ΣxΣy / nΣx^2 - (Σx)^2
def slope(x, y):
  x = np.array(x)  
  y = np.array(y) 
  n = np.size(x)

  nΣxy = n * np.sum(x * y)
  ΣxΣy = x.sum() * y.sum()
  nΣx_exp2 = n * np.sum(x ** 2)
  Σx_exp2 = x.sum() ** 2
  m = (nΣxy - ΣxΣy) / (nΣx_exp2 - Σx_exp2)
  return np.round(m, 4)

#y intercept function, formula: Σy - mΣx / n
def y_intercept(x, y):
  x, y, n, m = np.array(x), np.array(y), len(x), slope(x, y)
  Σy = y.sum()
  mΣx = m * x.sum()
  b = (Σy - mΣx) / n
  return np.round(b, 4)


x = wholePhone
y = wholeSleep
m = slope(x,y)
b = y_intercept(x,y)

print("Slope: ", m)
print("Y-Intercept: ", b)

y_predicted = []

for i in range(len(x)):
  y_pred = m * x[i] + b
  y_predicted.append(y_pred)

#Plotting the Regression Line
plt.plot(x, y_predicted, linestyle = 'solid', color = 'black', label="Regression")
#Placement of Legend
plt.legend(loc="upper right")




#COVARIANCE CALCULATIONS
x = wholePhone
y = wholeSleep
cov_mat = np.stack((x, y), axis = 0) 
print("Covariance Matrix:")
print(np.cov(cov_mat))
print("Covariance of Screen Time: ", np.cov(cov_mat[0]))
print("Covariance of Sleep Time: ", np.cov(cov_mat[1]))



#Showing the final graph
plt.show()