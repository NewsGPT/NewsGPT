import os
import openai
import json

openai.organization = "<OPENAI.ORGID>"
openai.api_key = "<OPENAI.APIKEY>"
print(openai.Model.list())


with open("Prompt_tmpl.txt", "r") as fin:
    prompt_tmpl_txt = fin.readlines()

prompt_tmpl = "".join(prompt_tmpl_txt)

news_json = json.load(open("china_news.json", "r"))

news_lines = []
for idx, i in enumerate(news_json['value']):
    news_lines.append(f"\nNews Item: {idx+1}:")
    news_lines.append("\n" + i["name"])
    news_lines.append("\n" + i["description"])
news_resutls = "".join(news_lines)

# format query, news search results from query
prompt = prompt_tmpl.format("taiwan", news_resutls)
print(prompt)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0,
  max_tokens=1200,
  top_p=0.33,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)