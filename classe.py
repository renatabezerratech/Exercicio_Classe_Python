# Na orientação a objeto o código é divido em objetos independentes (como se fossem miniprogramas);
# Cada objeto representa uma parte diferente da aplicação e cada objeto tem seus dados e sua lógica;
# Cada objeto pertence a uma classe e, esses objetos, possuem relacionamentos entre eles;
# A classe é a descrição (a ideia) do objeto; Na classe tem os atributos (Propriedades) e os comportamentos (métodos);
# Exemplo -->  CLASSE-pessoa  (Propriedade)ATRIBUTO-nome, idade  (Método)COMPORTAMENTO-falar ;
# Atributos armazenam informações sobre o objeto (variáveis) e os comportamentos são o que fazer (funções);
# Para criar uma classe use class e dê um nome;
# Pode ser indicado, entre os parênteses, se a classe vai herdar métodos de outra classe (coloca o nome);
# Quando não vamos usar métodos de outra classe, os parênteses ficam vazios;
# As instâncias criadas são variações do objeto (a classe é como um molde para as instâncias (criações));



class aprendendoClasse():
    def __init__(self): # Método construtor da classe (o self referencia o objeto e o init ativa a propriedade);
        self.meuAtributo = "construtor"

    def meuMetodo(self): # Será criado um método para impressão de mensagem na tela;
        print("meu Método") # Os métodos podem executar ações criadas pelo dev;   


# Vou criar o objeto do tipo -> aprendendoClasse:

def criaObjeto():
    meuObjeto = aprendendoClasse() # Aqui estou instanciando o objeto do tipo aprendendoClasse;
    x = meuObjeto.meuAtributo  # Aqui atribui o valor da variável para meuAtributo;
    print(x)
    meuObjeto.meuMetodo()  # Aqui executa o método (função);

# Executa a função:
criaObjeto()

