my_dict = {}
while True:
    print("\nDictionary Mini Book")
    print("1.Add a Word: ")
    print("2.Search For Meaning: ")
    print("3.Display all Words: ")
    print("4.Update Meaning:")
    print("5.Delete Word")
    print("6.Exit the Dictionary")

    choice = int(input("enter the Number you want: "))
    if choice ==1:
        word = input("Enter the word you want to add: ").lower()
        meaning = input("Enter the meaning of the input: ").lower()
        my_dict[word] = meaning
        print("your word is added Succesfully")
    elif choice ==2:
        search = input("Enter the word your are searching for: ").lower()
        if search in my_dict:
            worde = my_dict[search]
            print(f"Meaning : {worde}")
        else:
            print(f" your word {search} doesnt exists in this Dictionary")
    elif choice ==3:
        print("Words and their meaning")
        for i,j in my_dict.items():
           print(f"{i}:{j}")
    
    elif choice ==4:
    
        update_word = input("enter the word you want to update: ").lower()
        update_meaning = input("enter the meaning of the updated word: ").lower()
        my_dict[update_word] = update_meaning
    
        print("Meaning Updated Succesfully")
        print(f"update Meaning:{update_meaning}")
    elif choice == 5:
        delete_word = input("Enter the Word you want to delete: ").lower()
        if delete_word in my_dict:
            my_dict.pop(delete_word)
            print("Your word is deleted succesfully")
        else:
            print("your word doesnt exists")
    elif choice ==6:
        print("exiting the Program")
        break
    else:
        print("please enter the correct the number")
print("Hope you enjoyed the Dictionary mini book")

