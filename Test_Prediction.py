import math
start = 0
c = 0
time = 0
predict_time = 0
Nt = 0
No = 0
# Basic formula
#prediction = start * c ** time
No = int(input("No: "))
Nt = int(input("Nt: "))
time = int(input("Time: "))
NoPred = int(input("Prediction Start: "))
predict_time = int(input("PredictTime: "))

c = (Nt / No) ** (1/time)

prediction = NoPred * c ** predict_time

print(c)
print(prediction)
