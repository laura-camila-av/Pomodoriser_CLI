

import array as arr
from datetime import datetime, timedelta

if __name__ == "__main__":
    import taskPopulator
    import instructions
    import formatter
    from datetime import datetime, timedelta
    

    instructions.showInstructions()
    timeAvailable = taskPopulator.getPlanLength()
    unsortedPlans = []
    Adding = True

    rowCount = int(0)

    while rowCount < timeAvailable: #should change this conditional to depend on amount time of time left?
        taskName = taskPopulator.requestTaskName()
        pomodoroNo = taskPopulator.requestTaskTime()
        if (int(pomodoroNo) + rowCount) >= timeAvailable:
            print("Adding this plan will take you to the end of your time limit.\nTasks exceeding the time limit will not be included in the plan.")
        taskPriority = taskPopulator.requestTaskPriority()
        new_task = taskPopulator.insertAtribute(taskName, pomodoroNo, taskPriority)
        taskPopulator.appendTask(unsortedPlans, new_task)
        #userIsDone = str(input("To add another tasks, press enter 'C'.\nTo stop adding tasks and generate the plan, enter 'G'."))
  
            #This will debugged out in future versions when the program goes beyond the command line.
        rowCount += int(pomodoroNo)

    print("You have filled all the available time. Your plan will now be generated.")

    sortedPlans = taskPopulator.sortByPriority(unsortedPlans)

    taskPopulator.assignRanks(sortedPlans)
  
    startTime = formatter.getStartTime()
    times = formatter.createTimesList(startTime, sortedPlans)
    formatted_plan = formatter.fillTable(sortedPlans, times)
    print(formatted_plan)
