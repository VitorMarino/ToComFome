from Projeto_DSI import *



# Classe Entregador:

class ENTREGADOR(Base):
    __tablename__ = 'ENTREGADOR'
    id_entregador = Column('CPF', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME',String(255), nullable=False)
    telefone = Column('TELEFONE', String(15), nullable=False)


    def __init__(self, id_entregador, nome, telefone):
        self.id_entregador = id_entregador
        self.nome = nome
        self.telefone = telefone


# Model da classe Entregador:


class Model_Entregador():

    def __init__(self):
        self.entregadores = []
        
    def adicionar_entregador(self, entregador):
        self.entregadores.append(entregador)
        
    def buscar_entregador(self, entregador_id):
        for entregador in self.entregadores:
            if entregador.id_entregador == entregador_id:
                return entregador
        return None
    
    def associar_entregador_pedido(self, entregador_id, pedido_id):
        entregador = self.buscar_entregador(entregador_id)
        if entregador:
            pedido_controller = Model_Pedido()
            pedido = pedido_controller.buscar_pedido(pedido_id)
            if pedido:
                pedido.entregador = entregador
                return True
        return False
    
# A classe Model_Entregador permite adicionar novos entregadores 
# e buscar entregadores pelo ID.


#-- Referente a função associar_entregador_pedido
# Nessa função, estamos primeiro procurando o entregador 
# pelo entregador_id. Em seguida, criamos uma instância do 
# Model_Pedido para buscar o pedido pelo pedido_id. Se 
# ambos, o entregador e o pedido, existirem, então associamos o 
# entregador ao pedido definindo pedido.entregador = entregador 
# e retornamos True. Caso contrário, retornamos False.

# Note que, para que essa função funcione corretamente, 
# é necessário adicionar um atributo entregador à classe 
# Pedido, que pode ser definido na inicialização da classe 
# Pedido como self.entregador = None. Isso permitirá que associemos 
# um entregador a um pedido.