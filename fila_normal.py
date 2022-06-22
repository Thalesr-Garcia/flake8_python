from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_tual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}')
