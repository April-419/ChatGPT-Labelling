import openai

openai.api_key = "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"

def label_gender(first_name):

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a gender labeller."},
            {"role": "user", "content": f"In one word, what is the gender of the person with the first name: {first_name}? Say only: 'Male', 'Female' "}
        ])

    message = response.choices[0]['message']
    return message['content']


def label_ethnicity(last_name):
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are an ethnicity labeller."},
            {"role": "user", "content": f"What is the ethnicity of the person with the last name: {last_name}? Without explaining, say only: 'British-origin', 'Chinese', 'Middle Eastern', 'Eastern European', 'Indian', 'non-Chinese East Asian','Southern European and Hispanic', 'Western & Northern European', or 'African' "}
        ])

    message = response.choices[0]['message']
    return message['content']
