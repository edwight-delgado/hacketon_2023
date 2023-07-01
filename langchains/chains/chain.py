class Chain:
    def __init__(self, prompt_template, input_variables):
        self.template = prompt_template
        self.variable = variable

    def prompt_response(self):
        prompt_template = PromptTemplate(template=self.template, input_variables=['language'])
        # creamos el primer chain con el saludo
        return LLMChain(llm=llm, prompt=prompt_template)


# Chain 1
# creamos el primer string del template
template = "Eres un experto en programación, explica cómo se inicializa una variable en {language}."
# cargamos el primer template con las variables
prompt_template = PromptTemplate(template=template, input_variables=['language'])
# creamos el primer chain con el saludo
var_chain = LLMChain(llm=llm, prompt=prompt_template)

# Chain 2
# creamos el segundo string del template
template = "Eres un experto en programación, explica cómo se realiza un loop en {language}."
# cargamos el segundo template con las variables
prompt_template = PromptTemplate(template=template, input_variables=['language'])
# creamos el segundo chain con el saludo
loop_chain = LLMChain(llm=llm, prompt=prompt_template)



# ya tenemos las dos cadenas creadas, ahora las ejecutamos
from langchain.chains import SimpleSequentialChain

template = "Eres un experto en programación, explica cómo se inicializa una variable en {language}."
input_variables=['language']
chain1 = Chain(template, input_variables)
response1 = chain1.prompt_response()

template = "Eres un experto en programación, explica cómo se inicializa una variable en {language}."
input_variables=['language']
chain2 = Chain(template, input_variables)
response2 = chain2.prompt_response()


conversa_chain = SimpleSequentialChain(chains=[response1, response2], verbose=True)
conversa_chain.run('javascript')