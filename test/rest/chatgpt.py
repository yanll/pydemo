import openai

openai.api_type = "azure"
openai.api_base = "https://yp2401.openai.azure.com/"
openai.api_key = "2fcbec6687ec42b481bede40fbfcca15"
openai.api_version = "2023-09-01-preview"

response = openai.ChatCompletion.create(
    engine="YPgpt",
    messages=[
        {"role": "system", "content": "现在几点了？"},
        {"role": "user", "content": "明天天气怎样？"},
        {"role": "assistant", "content": "健身可以减肥吗？"},
        {"role": "user", "content": "有什么好听的歌曲推荐吗？"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
