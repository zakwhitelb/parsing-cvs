from bson import ObjectId

def convert_objectid_to_str(data):
    """
    Recursively convert ObjectId fields to strings in a dictionary or list.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
            elif isinstance(value, (dict, list)):
                convert_objectid_to_str(value)
    elif isinstance(data, list):
        for item in data:
            convert_objectid_to_str(item)
    return data