import openai
import streamlit as sl

openai.organization = sl.secrets["organization"]
openai.api_key =  sl.secrets["key"]
password =  sl.secrets["password"]

if password != sl.text_input("Enter password"): exit(600)

temp = sl.sidebar.slider("Craziness of ideas",0.0,2.0,0.5)
model = sl.sidebar.radio("model to use",("text-davinci-003","gpt-3.5-turbo-0301"))


originating_text = sl.text_area("enter starting text")
scenario = sl.text_input("Enter prompt")

def davinci(text):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=text,
      temperature=temp,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response

def turbo(whoami, text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      messages= [
          {"role": "system", "content": whoami},
          {"role": "user", "content": text}
      ],
      temperature=temp,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response
if model == "gpt-3.5-turbo-0301":
    whoami = sl.sidebar.text_input("Who is the AI assistant?")


go = sl.button("do it!")

if go:
    sl.sidebar.text("Submitting to the AI Gods....")

    sl.write(scenario+originating_text)

    if model == "text-davinci-003":
        response = davinci(scenario+originating_text)
        sl.write(response)
        AI_scenario = response["choices"][0]["text"]
        sl.write(AI_scenario)
    elif model == "gpt-3.5-turbo-0301":
        response = turbo(whoami, scenario+originating_text)
        sl.write(response)
        #AI_scenario = response["choices"][0]["text"]
        #sl.write(AI_scenario)



    #sl.subheading("Result as a CSV string")
    #lines = [line.strip() for line in AI_scenario.splitlines() if line.strip()]
    #lines = [re.sub("^\d+\.", "", line) for line in lines]
    #comma_separated_string = ", ".join(lines)

    #sl.write(comma_separated_string)
