import json
from watson_developer_cloud import AssistantV1

assistant = AssistantV1(
    username='d662d4ba-9e5d-4631-b94b-23446011f580',
    password='HlfulHf7UuJQ',
    version='2018-09-20',
    #url='https://gateway.watsonplatform.net/assistant/api'
)

response = assistant.message(
    workspace_id='d44da73a-4abb-4cd0-9ab1-803488fdec1f',
    message_input={
        'text': ''
    }
).get_result()

print(json.dumps(response, indent=2))