import time
print("|---------------------------------------------|")
print(" MINI PROJECT OF GAME AND OTHER COMPONENTS    ")
print("|---------------------------------------------|")
print("                           developed by Aman chauhan")
time.sleep(2)
# print("Enter your name please!")
name = str(input("Enter you name here\n"))
contact = input("Eneter your mobile number\n")
address = str(input("Enter your Address here\n"))
print(f"Thank you! {name} for entering your informatioon here")
print("We have many types of projects available, Like:\n")
print("[1] Pizza bill [2] Shoes Bill [3] Snake, Water, Gun [4] Stone, Paper, Scissor")
choice = int(input("Enter [1] Pizza bill [2] Shoes Bill [3] Snake, Water, Gun [4] Stone, Paper, Scissor\n"))
if choice == 1:
    import pizza_bill
    print(pizza_bill)
    print(f"Thank you {name} for using our project\n")
elif choice == 2 :
    import shoes_program
    print(shoes_program)
    print(f"Thank you {name} for using our project\n")
elif choice == 3 :
    import snake_water_gun
    print(snake_water_gun)
    print(f"Thank you {name} for using our project\n")
elif choice == 4 :
    import stone_paper_scissor_game
    print(stone_paper_scissor_game)
    print(f"Thank you {name} for using our project\n")
else :
    print("ERROR!! sorry you entered the wrong input.")


with open("project.txt","a") as f:
    f.write(name)
    f.write("\n")
    f.write(contact)
    f.write("\n")
    f.write(address)
    f.write("\n")

    

