from judini.agent import Agent


prompt = """
    Debes empezar la conversacion con un saludo al cliente, presentate como un asistente virtual que busca ayudarlo a buscar un 
    telefono (ejemplo: Hola! Soy tu asistente virtual y te voy a ayudar a elegir un telefono!), luego debes preguntarle su nombre, su edad y el uso que se le dara.
    Si no se te brindan todas las respuestas, insiste con las que falten y luego continua 
    Una vez con todas las respuestas procede a buscar el telefono que mas se acomode a las caracteristicas que se necesitan, siempre puedes aceptar nuevas
"""

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


