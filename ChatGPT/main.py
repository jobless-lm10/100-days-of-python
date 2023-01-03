import os

import openai

# Set up the API client
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.api_client.API()

# Generate text using the GPT engine
response = client.engine("davinci").completion(
    engine="davinci",
    prompt="The quick brown fox jumps over the lazy dog. ",
    max_tokens=100,
    temperature=0.7,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
)

# Print the generated text
generated_text = response["choices"][0]["text"]
print(generated_text)



