from abc import ABC, abstractmethod
class P_motorista(ABC):
    @abstractmethod
    def adicionar(self):
        pass

    @abstractmethod
    def editar(self):
        pass

    @abstractmethod
    def deletar(self):
        pass

    @abstractmethod
    def buscar_motorista(self):
        pass

class P_veiculos():
    @abstractmethod
    def adicionar(self):
        pass

    @abstractmethod
    def editar(self):
        pass

    @abstractmethod
    def deletar(self):
        pass

class P_viagens():
    @abstractmethod
    def adicionar(self):
        pass

    @abstractmethod
    def editar(self):
        pass

    @abstractmethod
    def deletar(self):
        pass

class Abastacimento():
    @abstractmethod
    def adicionar_ab(self):
        pass

    @abstractmethod
    def imprimir_ab(self):
        pass


class Manutenções():
    @abstractmethod
    def adicionar_m(self):
        pass
    @abstractmethod
    def imprimir_m(self):
        pass
    @abstractmethod
    def total_man(self):
        pass
