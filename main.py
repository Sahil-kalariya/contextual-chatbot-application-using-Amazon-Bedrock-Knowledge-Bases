# Import the required libraries:
import json
import boto3

def getResponse():
    region_name = ''
    kb_id = ''
    # try out KB using RetrieveAndGenerate API
    bedrock_agent_runtime_client = boto3.client("bedrock-agent-runtime", region_name=region_name)
    model_id = "anthropic.claude-instant-v1" # try with both claude instant as well as claude-v2. for claude v2 - "anthropic.claude-v2"
    model_arn = f'arn:aws:bedrock:{region_name}::foundation-model/{model_id}'

    # Query using your own question
    query = "color of sky"
    response = bedrock_agent_runtime_client.retrieve_and_generate(
        input={
            'text': query
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kb_id,
                'modelArn': model_arn
            }
        },
    )
    generated_text = response['output']['text']
    print(generated_text)

if __name__ == "__main__":
    getResponse()



# {'id': 'msg_bdrk_01GNeNzo4ZjAguvfqGkkVV9M', 'type': 'message', 'role': 'assistant', 'model': 'claude-3-sonnet-20240229', 
# 'content': [{'type': 'text', 'text': "Hello! As an AI language model, I don't have subjective experiences or emotions, but I'm operating properly and ready to assist you with any questions or tasks you might have. How can I help you today?"}], 
# 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 13, 'output_tokens': 47}}