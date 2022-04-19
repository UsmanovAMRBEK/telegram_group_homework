import json

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    user_messages = {}
    for user in data['messages']:
        if user['type']=="message" and user["from_id"]==users_id:
            user_messages[users_id] = user_messages.get(users_id, 0) + 1
    return user_messages
f=open("./data/result.json")
data=json.load(f)
f.close()