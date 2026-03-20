def insertAtribute(taskName, pomodoroNo, taskPriority):
    new_task = list(range(5))
    new_task[1] = taskName
    new_task[2] = pomodoroNo
    new_task[3] = taskPriority
    print(new_task)#function to check the input doesn't exceed the maximum length capacity (to protect neat table formatting)

#def createTask():
    #Task created with placeholder values

    #Index 3 is for priority, Index 4 is for task length
    #new_task = list(range(5))
    #return new_task

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
#taskName = requestTaskName()

def requestTaskTime():
    timeUnit= str(input("Estimate how long you think it will take to complete the task. \nFirst, specify if your estimate is in hours, minutes or number of Pomodoro sessions. \nFor hours, enter H, for minutes, enter M and for Pomodoro (25 minutes) enter P."))
    validTimeUnits = ['h','H','M','m','P','p']
    
    def isNumber(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
    while timeUnit not in validTimeUnits or isNumber(timeUnit):
        print("The time unit you entered is in valid.")
        timeUnit = (input("For hours, enter H, for minutes, enter M and for Pomodoro (25 minutes) enter P."))
    
    #need to fix a bug which results in a letter going in index 2 if the user first enters a letter by accident, need to reset it

    if timeUnit == 'H' or timeUnit == 'h':
        taskTime = float(input("Enter your estimate of how long it will take to complete the task in HOURS."))
        while isNumber(taskTime) == False:
            taskTime = float(input("You did not enter a number.\nPlease try again to enter your estimate of how long it will take to complete the task in HOURS."))
            return isNumber(taskTime)
        pomodoroNo = taskTime * 2.4
        pomodoroNo = int(round(pomodoroNo, 0))
        return pomodoroNo

    elif timeUnit == 'M' or timeUnit == 'm':
        taskTime = int(input("Enter your estimate of how long it will take to complete the task in MINUTES."))
        while isNumber(taskTime) == False:
            taskTime = float(input("You did not enter a number.\nPlease try again to enter your estimate of how long it will take to complete the task in MINUTES."))
            return isNumber(taskTime)
        pomodoroNo = taskTime / 25
        pomodoroNo = int(round(pomodoroNo, 0))
        return pomodoroNo
    
    elif timeUnit == 'p' or timeUnit == 'P':
        pomodoroNo = (input("Enter your estimate of how long it will take to complete the task in number of POMODORO sessions."))
        while isNumber(pomodoroNo) == False:
            pomodoroNo = float(input("You did not enter a number.\nPlease try again to enter your estimate of how long it will take to complete the task in MINUTES."))
            return isNumber(pomodoroNo)
        return int(pomodoroNo)
    

#pomodoroNo = requestTaskTime()

def requestTaskPriority():
    taskPriority = int(input("Rate the priority of this task from 1-5. 1 is highest priority and 5 is lowest priority. If you do not wish to give this task a priority, enter 5."))
    while taskPriority not in [1,2,3,4,5]:
        taskPriority = int(input("Your rating must be between 1 and 5. If you do not wish do give it a priority, enter 5."))
    return taskPriority

#taskPriority = requestTaskPriority()


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
        


