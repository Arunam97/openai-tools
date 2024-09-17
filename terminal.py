from openai_util.openai_api import prompt

def main():
    messages = []
    
    while True:
        print("--------------------------------------")
        user_input = input("You: ")

        messages.append({"role": "user", "content": user_input})
        
        try:
            response, messages = prompt(messages)
            print("--------------------------------------")
            print(f"Assistant: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
