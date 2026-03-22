#taskPopulator.py
def getPlanLength():
    planLength = input("How long, in number of pomoodoro sessions would you like this plan to be?\nNote that pomodoro sprint is 30 minutes long.")
    while isNumber(planLength) == False:
        planLength = input("The value you entered is invalid. It must be a number greater than zero.")
    return int(planLength)


def checkInputLength(field):
    if len(field) > 50:
        return True
    else:
        return False

 #need to make this a more generic function that can be recycled for all of the inputs   
 #I decided to make this function just for the name because the other inputs have to be manipulated before being added to the list.
def requestTaskName():
    taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
    exceedsMaxLength = checkInputLength(taskName)
    while exceedsMaxLength or len(taskName) == 0:
        print("Your description is either empty or too long. PLease re-enter a description that does not exceed 50 characters.")
        taskName = str(input("Enter a brief description of the task you wish to complete then click enter."))
        exceedsMaxLength = checkInputLength(taskName)
    return taskName

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def requestTaskTime():
    timeUnit= str(input("Estimate how long you think it will take to complete the task. \nFirst, specify if your estimate is in hours, minutes or number of Pomodoro sessions. \nFor hours, enter H, for minutes, enter M and for Pomodoro (25 minutes) enter P."))
    validTimeUnits = ['h','H','M','m','P','p']
   
    while timeUnit not in validTimeUnits or isNumber(timeUnit):
        print("The time unit you entered is in valid.")
        timeUnit = (input("For hours, enter H, for minutes, enter M and for Pomodoro (25 minutes) enter P."))
  
    if timeUnit == 'H' or timeUnit == 'h':
        taskTime = (input("Enter your estimate of how long it will take to complete the task in HOURS."))
        while isNumber(taskTime) == False:
            taskTime = (input("You did not enter a number.\nPlease try again to enter your estimate of how long it will take to complete the task in HOURS."))
        
        pomodoroNo = taskTime * 2.4
        pomodoroNo = int(round(pomodoroNo, 0))
        return pomodoroNo

    elif timeUnit == 'M' or timeUnit == 'm':
        taskTime = (input("Enter your estimate of how long it will take to complete the task in MINUTES."))
        while isNumber(taskTime) == False:
            taskTime = (input("You did not enter a number.\nPlease try again to enter your estimate of how long it will take to complete the task in MINUTES."))
        
        pomodoroNo = taskTime / 25
        pomodoroNo = int(round(pomodoroNo, 0))
        return pomodoroNo
    
    elif timeUnit == 'p' or timeUnit == 'P':
        pomodoroNo = (input("Enter your estimate of how long it will take to complete the task in number of POMODORO sessions."))
        while isNumber(pomodoroNo) == False:
            pomodoroNo = (input("You did not enter a number.\nPlease try again to enter your estimate of how long it will take to complete the task in MINUTES."))
        return int(pomodoroNo)
  

def requestTaskPriority():
    taskPriority = (input("Rate the priority of this task from 1-5. 1 is highest priority and 5 is lowest priority. If you do not wish to give this task a priority, enter 5."))
    while isNumber(taskPriority) == False or int(taskPriority) not in [1,2,3,4,5]:
        taskPriority = (input("Your rating must be between 1 and 5. If you do not wish do give it a priority, enter 5."))
    return int(taskPriority)

#simplify this function as you progress by making it like this insertAtribute(field,index)
def insertAtribute(taskName, pomodoroNo, taskPriority):
    #new_task = createTask()
    new_task = list(range(5))
    #new_task[0] will be the index, this will be added after the tasks are in an array.
    new_task[1] = taskName
    new_task[2] = pomodoroNo
    new_task[3] = taskPriority
    return new_task

def appendTask(unsortedPlans,new_task):
    for _ in range(new_task[2]):
        unsortedPlans += [new_task.copy()]
    return unsortedPlans 
   
def sortByPriority(unsortedPlans):
    return sorted(unsortedPlans, key=lambda x: x[3])

def assignRanks(sortedPlans):
    for i in range(len(sortedPlans)):
        sortedPlans[i][0] = i + 1

#def assignTimes(sortedPlans)
    
    #for t in range(len(sortedPlans)):
        #sortedPlans[i][1] = t + 30
        


