class InscricaoDTO:
    def __init__(self, nome: str, email: str, dataNascimento: str = None, evento: int = None):
        self.nome = nome
        self.email = email
        self.dataNascimento = dataNascimento
        self.evento = evento