import json


def load_data(path):
    """
    Opens the json file at path location (from current dir)

    Parameters
    ----------
    path: str
        Path to json file

    Returns
    -------
    json_data: {}
        Data
    """
    with open(path, 'r') as f:
        json_data = json.load(f)
    return json_data


def get_path(themes, selected_theme):
    """
    Returns the path of the dowloaded file. Useful in case several themes have
    been downloaded

    Parameters
    ----------
    themes: [str]
        List of themes
    selected_theme: int
        Item number

    Returns
    -------
    path: str
        Path to relevant theme data
    """
    for theme, link in themes.items():
        if int(theme[0]) == selected_theme:
            path = './data/' + theme[2:] + '.json'
    return path


def load_question(questions_id, data_theme_json, question):
    """
    Loads the data associated to the selected question in a dict

    Parameters
    ----------
    question_id: str
        Question ID
    data_theme_json: {}
        Data bearing all questions
    question: str
        Question to filter

    Returns
    -------
    data_theme_response_dict: {}
        Only relevant responses
    """
    data_theme_response = [(r['questionId'], r['formattedValue']) for x in data_theme_json for r in x['responses']]
    data_theme_response_dict = {x: [] for x in questions_id}
    for x in data_theme_response:
        if x[1]:
            data_theme_response_dict[x[0]].extend([x[1]])
    return data_theme_response_dict
