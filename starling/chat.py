import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate


class Chat:

  def __init__(self):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    self.history = []
    # self.persist_directory = "chat/chroma/"
    # self.embeddings = OpenAIEmbeddings()
    # self.vectordb = Chroma(
    #   persist_directory=self.persist_directory,
    #   embedding_function=self.embeddings
    # )
    self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    response = self.llm.predict("What is the capital of France?")
    print(response)
    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    human_template = "{text}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])
    formatted_message = chat_prompt.format_messages(input_language="English",
                                                    output_language="French",
                                                    text="I love programming.")
    print(formatted_message)
    self.history.append(formatted_message)
    chain = chat_prompt | self.llm
    response = chain.invoke(formatted_message)
    print(response)

  def chat(self, question):
    self.history.append(prompt)
    response = openai.ChatCompletion.create(model=self.llm,
                                            messages=[{
                                                "role": "user",
                                                "content": f"{question}"
                                            }],
                                            temperature=0.8)
    return response.choices[0].text.strip()

  def chat_loop(self):
    while True:
      prompt = input("You: ")
      if prompt.lower() == "quit":
        break
      response = self.chat(prompt)
      print("Starling:", response)
      self.history.append(response)


if __name__ == "__main__":
  chat = Chat()
  # chat.chat_loop()
