def sanitize_input(user_input):
    """
    Cleans the input string by removing unwanted characters.
    :param user_input: str
    :return: str
    """
    import re
    return re.sub(r'[^a-zA-Z0-9 ]', '', user_input).strip()