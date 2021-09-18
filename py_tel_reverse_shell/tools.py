from .Engine import engine

def get_last_message(bot_token):
    response = engine.receive_message(bot_token)
    
    message_id = response[-1]['message']['message_id']
    message_text = response[-1]['message']['text']
    
    result = {"text":message_text,"id":message_id}
    
    return result
