#Opening page

#Eventually could break down insert attribute so tasks are added once at a time.
import array as arr

if __name__ == "__main__":
    import taskPopulator
    import instructions
    import formatter
    

    instructions.showInstructions()
    unsortedPlans = []
    Adding = True

    while Adding:
        taskName = taskPopulator.requestTaskName()
        pomodoroNo = taskPopulator.requestTaskTime()
        taskPriority = taskPopulator.requestTaskPriority()
        new_task = taskPopulator.insertAtribute(taskName, pomodoroNo, taskPriority)
        taskPopulator.appendTask(unsortedPlans, new_task)
        userIsDone = str(input("To add another tasks, press enter 'C'.\nTo stop adding tasks and generate the plan, enter 'G'."))
        if userIsDone == 'c' or userIsDone == 'C':
            Adding = True
        else:
            Adding = False
    print("These are the raw unfiltered plans. In later versions this will be hidden and not printed until it is formatted as a table.")
    sortedPlans = taskPopulator.sortByPriority(unsortedPlans)
    taskPopulator.assignRanks(sortedPlans)
    print(sortedPlans)
    #header = formatter.planHeader()
    #print(header)
    formatted_plan = formatter.fillTable(sortedPlans)
    print(formatted_plan)



    #sortedPlan = taskPopulator.sortByPriority(unsortedPlans)
   #1
   

    
