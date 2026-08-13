def wake_up():
        while True:
            command=input("Hello! I am Friday, your personal assistant. How can I help you today? ").lower().strip()  
            process_command(command)
            
            

def process_command(command):
                if "hi"in command or "hello" in command or "hey friday" in command:         
                    print("Hello Sir! How can I assist you today?")
                elif command =="what is your name":         
                    print("My name is Friday, your personal assistant.")     
                elif command == "how are you":         
                    print("I am doing well, thank you for asking. How can I assist you today?")     
                elif command == "goodbye":         
                    print("Goodbye! Have a great day!")        
                else:         
                    print("I am sorry, I can only respond to 'hello', 'what is your name', 'how are you', 'hey friday', and 'goodbye' as wake words. Please try again.")
        
     
