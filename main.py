class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido')
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano invalido.')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print(f'O filme {filme} não está disponível para este plano. Faça upgrade para premium.')
        else:
            print('Plano inválido.')


        

cliente = Cliente('Matheus', 'matheus@mail.com', 'basic')
print('O cliente', cliente.nome, 'tem o plano', cliente.plano)
cliente.ver_filme('Harry Poter', 'premium')

print('-'*10)

# cliente com upgrade de plano
cliente.mudar_plano('premium')
print('O cliente', cliente.nome, 'tem o plano', cliente.plano)
cliente.ver_filme('Harry Poter', 'premium')