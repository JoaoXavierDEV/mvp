from pydantic import BaseModel


class PessoaSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    produto_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"
