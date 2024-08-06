import random
questions = {
    1:{
        "question" : "Which of the following is the correct extension of the Python file?",
         "option" : ["A. .python", "B. .pl;", "C. .py", "D. .p"],
         "answer" : "C" 
    },
    2:{
        "question" : "What do we use to define a block of code in Python?",
        "option" : ["A. Curly braces", "B. Parentheses", "C. Indentation", "D. Square brackets"],
        "answer" : "C"
    },
    3:{
        "question" : "Which keyword is used for function in Python?",
        "option" : ["A. def", "B. fun", "C. define", "D. function"],
        "answer" : "A"
    },
    4:{
        "question" : "Which of the following is not a core data type in Python?",
         "option" : ["A. List", "B. Dictonary", "C. tuples", "D. Class"],
         "answer" : "D" 
    },
    5:{
        "question" : "What is the output of the following code: print(2 ** 3)?",
         "option" : ["A. 8", "B. 6", "C. 11", "D. 9"],
         "answer" : "A" 
    },
    6:{
        "question" : "Which of the following is used to create an empty set in Python?",
         "option" : ["A. {}", "B. ()", "C. []", "D. set{}"],
         "answer" : "D" 
    },
    7:{
        "question" : "What is the output of the following code: print(type([]))?",
         "option" : ["A. <class 'list>", "B. <class 'tuple'>", "C. <class 'dictionary'>", "D. <class 'set'>"],
         "answer" : "A" 
    },
    8:{
        "question" : "Which of the following is the correct way to declare a variable in Python?",
         "option" : ["A. var x = 10", "B. x = 0", "C. int x = 10", "D. let x = 10"],
         "answer" : "B" 
    },
    9:{
        "question" : "Which of the following functions is used to find the length of a string in Python?",
         "option" : ["A. len()", "B. length()", "C. size()", "D. count()"],
         "answer" : "A" 
    },
    10:{
        "question" : "What is the correct syntax to output the type of a variable or object in Python?",
         "option" : ["A. print(typeof(x))", "B. print(type(x))", "C. print(typeOf(x))", "D. print(Typeof(x))"],
         "answer" : "B" 
    }
}

total_que = len(questions)
score = 0
que_list = []
name = input("Enter Your Name : ")
yes_no = input("Are you want to playing quiz (y/n) : ")
if(yes_no == "y" or yes_no == "Y"):
    for i in range(1, 11):
        while True:
            random_que_no = random.randint(1,10)
            if random_que_no not in que_list:
                que_list.append(random_que_no)
                break
        print(random_que_no)
        print("*"*70)
        print(f"Q{i}.",questions[random_que_no]["question"])
        print("\t",questions[random_que_no]["option"][0])
        print("\t",questions[random_que_no]["option"][1])
        print("\t",questions[random_que_no]["option"][2])
        print("\t",questions[random_que_no]["option"][3])
        choice = input("Enter your choice : ").upper()
        if(choice == questions[random_que_no]["answer"]):
            # print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer! Try Again!")
elif(yes_no == "n" or yes_no == "N"):
    print(f"Thank you {name}. You are not interest")
    
else:
    print(f"{name}, you press wrong key")
    
print("*"*70)
print(f"{name}, your score is {score}/{total_que}")
if score <=4:
    print("Need to work hard")
elif score == total_que:
    print("Excelent")
else:
    print("Good")

print("Over quiz!")