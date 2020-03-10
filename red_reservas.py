import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkRed1') # Cor da janela(tema)
        # Layout
        layout = [ # Definido estilos da janela
            [sg.Text('Nome do Cliente',size=(20,2)),sg.Input(size=(20,2),key='nome')], # nome da label
            [sg.Text('Data da Reserva',size=(20,2)),sg.Input(size=(20,2),key='data')],
            [sg.Text('Tipo da Reserva',size=(20,2)),sg.Input(size=(20,2),key='tipo')],
            [sg.Text('Consuma em R$',size=(20,2)),sg.Input(size=(20,2),key='consuma')],
            [sg.Button('Confirmar Reserva')]
        ]

        # Janela
        self.janela = sg.Window("Hookah Booker 1.0").layout(layout)



    def Iniciar(self):
        while True:
            # Extrair dos dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            data = self.values['data']
            tipo = self.values['tipo']
            consuma = self.values['consuma']


            # Armazenamento em TXT
            arquivo = open('arq01.txt', 'a')
            print(f'Nome: {nome}\n')
            print("\n")
            print(arquivo.write('Nome cliente:' + str(nome)+'\n'))
            print('----------')
            arquivo.close()

            arquivo = open('arq01.txt', 'a')
            print(f'Data: {data}\n')
            print("\n")
            print(arquivo.write('Data reserva: ' + str(data)+'\n'))
            print('----------')

            arquivo.close()

            arquivo = open('arq01.txt', 'a')
            print(f'Tipo: {tipo}')
            print("\n")
            print(arquivo.write('Tipo Reserva: ' + str(tipo)+ '\n'))
            print('----------')
            arquivo.close()

            arquivo = open('arq01.txt', 'a')
            print(f'Consuma: {consuma}')
            print("\n")
            print(arquivo.write('Valor Consuma: ' + str(consuma)+'\n'))
            print('----------')
            arquivo.close()

            print()
            print('----------')

    def criarRelatorio(self, nome, data, tipo, consuma):
        open('arq01.txt', 'a')
        arquivo2 = open('arq01.txt','w')



tela = TelaPython()
tela.Iniciar()


