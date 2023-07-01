from judini.agent import Agent



class MyAgent:
    def __init__(self, agent_id):
        # Replace with your actual API key and URL ID
        api_key = "298e14d9-b980-4865-8d8c-7902b30df614"
        agent_id = agent_id

        # Initialize the Judini class
        self.agent_instance = Agent(api_key, agent_id)


    def get_response(self, prompt):

        # Make a completion request
        return  self.agent_instance.completion(prompt, stream=False)


