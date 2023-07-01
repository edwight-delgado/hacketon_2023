from POE import load_chat_id_map, clear_context, send_message, get_latest_message, set_auth

#Auth
set_auth('Quora-Formkey','40a242d49c1656e38b246bb6912793b1')
set_auth('Cookie','m-b=iUlCMqc5laQ4vUNk4m-O0Q==')

def chatbot(message = '', bot_name='capybara'):
    if message != '' and len(message) > 5 :
        chat_id = load_chat_id_map(bot_name)
        clear_context(chat_id)
        print("Context is now cleared")

        send_message(message,bot_name,chat_id)
        reply = get_latest_message(bot_name)
        print(f"{bot_name} : {reply}")


        return reply
    return ''

if __name__=="__main__":
    message = input("Human : ")
    print(message)
    r = chatbot(message=message)            
    print(r)