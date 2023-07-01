from POE import load_chat_id_map, clear_context, send_message, get_latest_message, set_auth

#Auth
set_auth('Quora-Formkey','c8d14b9cad6c7f18d6e89f4318dcbd03')
set_auth('Cookie','m-b=SwOX76QP9Scv8nwJIL3QbA==')

msg = ''
def bot(message = '', bot_name='capybara'):
    chat_id = load_chat_id_map(bot)
    clear_context(chat_id)
    print("Context is now cleared")
    while True:
        message = input("Human : ")
        if message =="!clear":
            clear_context(chat_id)
            print("Context is now cleared")
            continue
        if message =="!break":
            break
        send_message(message,bot,chat_id)
        reply = get_latest_message(bot)
        print(f"{bot} : {reply}")


    return msg

if __name__=="__main__":
    message = input("Human : ")
    print(message)
    option = input("Please enter your choice : ")
    botss = {1:'capybara', 2:'beaver', 3:'a2_2', 4:'a2', 5:'chinchilla', 6:'nutria'}
    bot_name = botss[int(option)]
    print("The selected bot is : ", bot_name)
    r = bot(message=message,bot_name=bot_name)            
    print(r) 