"""__author__ = Kieran Wood

Description:
    A set of utilities to help serialize data

Testing:
    Run the file directly from terminal $ python3 kusu/serialization.py

TODO:
    * Add serialization and deserialization for YAML
"""
import os
import json
from validation import validate_extension

def save_to_json(data, file_path = os.path.join(os.getcwd(),"test"), file_name = "config.json"):
    """Serializes provided data to json file

    Args:
        data (str): JSON formatted data (Dictionary and/or class instance with vars(<instance>))
        file_path (str): The desired directory path to save the file out to
        file_name (str): The name of the output file
    """
    # TODO: Check for right extension in file_name
    with open(os.path.join(file_path, file_name), 'w') as write_file:
        json.dump(data, write_file)

def deserialize_json(file_path = os.path.join(os.getcwd(),"test"), file_name = "config.json"):
    """Deserializes provided json file to dictionary

    Args:
        data (str): JSON formatted data (Dictionary and/or class instance with vars(<instance>))
        file_path (str): The desired directory path to save the file out to
        file_name (str): The name of the output file

    Returns:
        Dict[]: Dictionary of all key-value pairs from JSON file
    """
    import json
    full_path = os.path.join(file_path, file_name)
    with open(full_path, 'r') as open_file:
        data = json.load(open_file)
    return data 

if __name__ == "__main__":
    test_data = {"name":"John Doe",
    "Age":19,
    "email": "example@example.com"
    }
    print("Saving test data to JSON file")
    save_to_json(test_data)
    print("Deserializing test data from JSON file")
    print(deserialize_json())