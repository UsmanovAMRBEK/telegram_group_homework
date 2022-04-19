import json

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    users_name = []
    for user in data["messages"]:
        if user.get("actor") and not (user.get("actor") in users_name):
            users_name.append(user.get("actor"))

    return users_name

f=open("./data/result.json")
data=json.load(f)
print(find_all_users_name(data))
f.close()
