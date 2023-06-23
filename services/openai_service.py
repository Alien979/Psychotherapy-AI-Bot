import openai

openai.api_key = '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'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful Psychotherapy AI Bot."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']
