from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  messages = [
    {
        "role": "system",
        "content": "You are a DJ with bricklaying skills and creative flair."
    },
    {
        "role": "user",
        "content": "Compose a 23 word sentence that explains the concept of universal healthcare."
    }
  ]
)

print(completion.choices[0].message)