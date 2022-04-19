import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    with open('./data/result.json') as json_file:
        data = json.load(json_file)
    return data