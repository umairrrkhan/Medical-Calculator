SIRS_score = 0


## Temperature

while True:
    temp= input('Enter the temperature ')
    try:
        temp =  float(temp)
    except ValueError:
        print('Please enter the value in the number')
        continue
    else:
        break

print(f"The temperature is : { temp}")

while True:
    if temp > 37.5 or temp < 36:
        SIRS_score+=1
        print('This is the abnormal ' , SIRS_score)
    else:
        print('This is noraml temperature')
        
    if temp > 40:
        print("This body temperature above 40 degrees Celsius can be life-threatening")
    else: 
        print('Fine!!!')

    print(f"Point: {SIRS_score}")
    break



## Respiratory System

while True:
    RespRate= input('enter the Respiratory Rate of the patient ? ')
    try:
        RespRate =  int(RespRate)
    except ValueError:
        print('Please enter the Whole number ? ')
        continue
    else:
        break

while True:
    PaCo2 = input('What is the patient PaCo2 ? (mmHg)')
    try:
        PaCo2 =  int(PaCo2)
    except ValueError:
        print('Please enter the Whole number ? ')
        continue
    else:
        break


print(f"this is the Respiratory Rate: { RespRate} , this is the PaCo2 of the patient {PaCo2}")

while True:
    if RespRate > 20 or PaCo2 < 32 :
        SIRS_score+=1
        print('this is the abnormal ' , SIRS_score)

    else:
        print('this is noraml Respiratory Rate and the PaCo2')
    if RespRate > 30 or PaCo2 < 20:
        print("A respiratory rate above 30 or a PaCo2 below 20 mmHg can indicate respiratory distress")
    else:
        print('Fine!!')
    print(f"Point: {SIRS_score}")
    break




## Heart Rate

while True:
    HeartRate= input('Enter the HeartRate ')
    try:
        HeartRate =  int(HeartRate)
    except ValueError:
        print('Please enter the value in the number')
        continue
    else:
        break

print(f"The Heart Rate is  : { HeartRate}")

while True:
    if HeartRate > 90:
        SIRS_score+=1
        print('this is the abnormal ' , SIRS_score)
    else:
        print('this is noraml HeartRate')
    if HeartRate > 120:
        print("A resting heart rate above 120 beats per minute can indicate tachycardia")
    else:
        print('Fine!!!')
    print(f"Point: {SIRS_score}")
    break


        
## White Blood Cell Count

while True:
    WhiteCell= input('Enter the White Cell (x10^9/L)')
    try:
        WhiteCell =  float(WhiteCell)
    except ValueError:
        print('Please enter the value in the number')
        continue
    else:
        break

print(f"The White Cell cont is is  : { WhiteCell}   x10^9/l")

while True:
    if WhiteCell > 12 or WhiteCell < 4:
        SIRS_score+=1
        print('this is the abnormal ' , SIRS_score)
    else:
        print('this is noraml White Cell count')
    if WhiteCell > 20:
        print("A white cell count above 20 x10^9/L can indicate a severe infection")
    else:
        print('Fine!!!!')
    print(f"Point: {SIRS_score}")
    break


## Red Blood Cell Count

while True:
    RedCell = input('Enter the Red Blood Cell Count (x10^12/L): ')
    try:
        RedCell = float(RedCell)
    except ValueError:
        print('Please enter the value as a number')
        continue
    else:
        break

while True:
    if RedCell < 3.5 or RedCell > 5.5:
        SIRS_score += 1
        print('This is abnormal.', SIRS_score)
    else:
        print('This is normal Red Blood Cell Count')
    
    if RedCell < 4.5:
        print("A low red blood cell count can lead to anemia")
    else:
        print("Fine!!!")
    
    print(f"Point: {SIRS_score}")
    break


## Report the Final Result

print(f"The total SIRS Score is: {SIRS_score}")

if SIRS_score >= 2:
    print("The criteria has been met. The patient has SIRS.")
else:
    print("The criteria has not been met. The patient does not have SIRS.")

