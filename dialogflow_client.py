""" Communicate with dialogflow API

function:
- detect_intent_texts
    args:
        - project_id: the id of your google project which has dialogflow api
        - session_id: sessions between endusers(discord users in channel) and dialogflow's agent
        - text
        - language_code
"""
import dialogflow_v2 as dialogflow


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text
