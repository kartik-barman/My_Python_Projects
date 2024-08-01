import os

#======Craete New File======# 

def create_file(fileName):
    try:
        with open(fileName, 'x') as f:
            print(f"File name {fileName} craeted successfully")
    except FileExistsError:
        print("File Already Exist!")

    except Exception as e:
        print('An Error Occured')


#======View All Files ======# 

def view_all_files():
    files = os.listdir()
    if not files:
        print("File not found!")
    else:
        for file in files:
            print(file)

#======Delete File======# 

def delete_file(fileName):
    try:
        os.remove(fileName)
        print(f"{fileName} has been deleted successfully!")
    except FileNotFoundError:
        print(f"{fileName} not found!")
    except Exception as e:
        print("An Error occurred")


#======Read File======# 

def read_file(fileName):
    try:
        with open(fileName, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{fileName} not found!")
    except Exception as e:
        print("An Error occurred")
        
#======Edit File======# 

def edit_file(fileName):
    try:
        with open(fileName, 'a') as f:
            content = input("Enter edit content : ")
            f.write(content + "\n")
            print(f"New Content added to {fileName} Successfully")
    except FileNotFoundError:
        print("File NOt Found!")
    
    except Exception as e:
        print("An Error Occurred")


def main():
    while True:
        print("File Management System")
        print("1. Create File")
        print("2. View all Files")
        print("3. Delete Files")
        print("4. Read Files")
        print("5. Edit Files")
        print("5. Exits")
    
        choice = input('Select your Choice (1-6) : ')
        
        if choice == '1':
            fileName = input('Enter Your Create File Name : ')
            create_file(fileName)
        
        elif choice == '2':
            view_all_files()
            
        elif choice == '3':
            fileName = input('Enter Your Delete File Name : ')
            delete_file(fileName)
        
        elif choice == '4':
            fileName = input('Enter Your Read File Name : ')
            read_file(fileName)
        
        elif choice == '5':
            fileName = input('Enter Your Edit File Name : ')
            edit_file(fileName)
        
        elif choice == '6':
            print('Closing this app....')
            break
        else:
            print('In-valid Syntax errors!')

if __name__=="__main__":
    main()
        