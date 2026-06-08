try :
    user = input("Enter your Name")
    feedback = input("Enter the Feedback")
    if not user:
        raise ValueError("Error Message : empty name .. enter your name")
    print(user)
    if not feedback :
        raise ValueError("Error message : please fill your feedback")
    print("\nThank you for your feedback!")
    print(feedback)  
except ValueError as error:
    print(error)
finally:
    ("program completed")
 


    