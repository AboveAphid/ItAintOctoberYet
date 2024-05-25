# GROQ is a great FREE alternative to openAI. Get a free unlimited API key from: https://console.groq.com/docs/api-keys

# pip install groq
from groq import Groq


class GroqInterface():
    def __init__(self, apiKey, model="llama3-8b-8192") -> None:
        self.apiKeySet = False
        if apiKey:
            self.apiKeySet = True
        self.apiKey = apiKey
        self.model = model
        try:
            self.client = Groq(api_key=self.apiKey)
        except ConnectionError:
            print("Could not connect to Groq using API KEY!")
        self.conversation = []

    def addToChat(self, role : str, content : str, printChat=False):
        
        if self.apiKey.strip() == "":
            return "Api Key not set!"

        try:
            if printChat:
                print(f'[{role.upper()}] {content.strip()}')

            self.conversation.append({"role": role, "content": content})

            chat_completion = self.client.chat.completions.create(
                messages=self.conversation,
                model=self.model,
            )

            response = chat_completion.choices[0].message.content

            self.conversation.append({"role": "assistant", "content": response})

            if printChat:
                print(f'\n[BOT] {response}\n')
        except:
            response = "Failed to generate! Please check that your API Key is valid!"

        return response
    
    def reset(self):
        self.conversation = []

    def updateAPIKey(self, apiKey, printChat=False):
        self.apiKey = apiKey
        self.client = Groq(api_key=self.apiKey)
        if printChat:
            print('Updated API Key!')




if __name__ == "__main__":
    import important

    groq = GroqInterface(important.groq_apiKey)

    groq.addToChat("system", important.mainStartingPrompt_Story, printChat=True)

    ans = groq.addToChat("user", """
    > There is a angry man with a shotgun aimed at you. He is made at you for stepping on his lawn.
    ? Bob Jankens
    : I try and reason with him while backing away slowly.
    """, printChat=True)
