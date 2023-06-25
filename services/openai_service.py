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
