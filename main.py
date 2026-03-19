#Opening page

#Eventually could break down insert attribute so tasks are added once at a time.
import array as arr

if __name__ == "__main__":
    import taskPopulator
    import instructions
    

    instructions.showInstructions()
    unsortedPlans = []
    Adding = True

    while Adding:
        taskName = taskPopulator.requestTaskName()
        pomodoroNo = taskPopulator.requestTaskTime()
        taskPriority = taskPopulator.requestTaskPriority()
        new_task = taskPopulator.insertAtribute(taskName, pomodoroNo, taskPriority)
        taskPopulator.appendTask(unsortedPlans, new_task)
        userIsDone = str(input("To add another tasks, press enter 'C'.\nTo stop adding tasks and generate the plan, enter 'Q'."))
        if userIsDone == 'c' or userIsDone == 'C':
            Adding = True
        else:
            Adding = False
    
    sortedPlans = taskPopulator.sortByPriority(unsortedPlans)
    print(sortedPlans)

    #sortedPlan = taskPopulator.sortByPriority(unsortedPlans)
   #1
   

    
