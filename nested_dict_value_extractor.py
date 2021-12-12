sample_dict = {"a": {"b": {"c": "d"}}}


def value_extractor(given_key, given_dict):
    """
    Extracts value from a dictionary for a given key

    :param given_key: key from a nested dictionary
    :param given_dict: python dictionary
    :return: value of the key
    """
    global result
    for k, v in given_dict.items():
        if k != given_key:
            if type(v) is dict:
                value_extractor(given_key, v)
        elif k == given_key:
            result = given_dict[k]
    return result


output = value_extractor("c", sample_dict)
print(output)
