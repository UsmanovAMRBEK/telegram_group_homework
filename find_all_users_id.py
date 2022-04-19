import json
def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users_id = []
    for user in data["messages"]:
        if user.get("actor_id") and not(user.get("actor_id") in users_id):
            users_id.append(user.get("actor_id"))
    for i in users_id:
        if 'channel' in i:
            users_id.remove(i)

    return users_id

f=open("./data/result.json")
data=json.load(f)
print(find_all_users_id(data))
f.close()