# Task management System

# invoke user to input task
# unvote the user to input unti the input 'exit' string
# once user exit the tak input print the task items


tasks=[]
while True:
    task=input("Enter your task or type exit to exit : ")
    
    if(task == "exit" ):
         for i in tasks:
            print(i)
         break
            
    else:
       
       tasks.append(task)
    