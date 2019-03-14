from random import randint
from FileRegister.RecordBattle import FileNameGenerator, WriteInFile, ResetNames

color = True

RegisterName = FileNameGenerator('FileRegister\BattleRecords\FileList')


def ChangeColor():
    global color

    if color:
        print('\33[1;34;0m')
    else:
        print('\33[1;31;0m')

    color = not color


class Player:
    def __init__(self, name='Manezao', attack=0, defense=0, agility=0, brutality=0, extraLife=0):
        """
        Cria um Objeto com a Classe Player
        :param name: nome do jogador
        :param attack: valor de ataque do jogador (0 - 3)
        :param defense: valor de defesa do jogador (0 - 3)
        :param agility: valor de agilidade do jogador (0 - 3)
        :param brutality: valor de brutalidade do jogador (0 - 3)
        :param extraLife: valor de vida extra do jogador (0 - 3)
        """
        self.__initialBars = (100, 8, 0, 10)
        self.__Attributes = {'attack': attack,
                             'defense': defense,
                             'agility': agility,
                             'brutality': brutality,
                             'extraLife': extraLife}
        self.__Life = self.__initialBars[0] + (20 * extraLife)
        self.__Stamina = self.__initialBars[1]
        self.__Critical = self.__initialBars[2]
        self.__Crystal = self.__initialBars[3]
        self.playerName = name

    # setMetods
    def SetLife(self, Life):
        """Atribui um valor para a Barra de Vida"""
        self.__Life = Life

    def SetCritical(self, Critical):
        """Atribui um valor para a Barra de Critico"""
        self.__Critical = Critical

    def SetStamina(self, Stamina):
        """Atribui um valor para a Barra de Energia"""
        self.__Stamina = Stamina

    def SetCrystal(self, Crystal):
        """Atribui um valor para a Barra de Cristal"""
        self.__Crystal = Crystal

    # getMetods

    def GetAttribute(self, atributName):
        """strength, defense, agility, brutality o extraLife"""
        return self.__Attributes[atributName]

    def GetAllAttributes(self):
        """Retorna os valores de todos os atributos como um dicionario"""
        return self.__Attributes

    def GetLife(self):
        """Retorna o valor da Barra de Vida"""
        return self.__Life

    def GetCritical(self):
        """Retorna o valor da Barra de Critico"""
        return self.__Critical

    def GetStamina(self):
        """Retorna o valor da Barra de Critico"""
        return self.__Stamina

    def GetCrystal(self):
        """Retorna o valor da Barra de Cristal"""
        return self.__Crystal

    def ShowAttributes(self):
        """Exibe todos os atributos no terminal"""
        for key, value in self.__Attributes.items():
            print(f'{key} : {value}')

    # Funções de acao do player

    def Turn(self, Opponent):
        """
        Chama o turno o Jogador e em sequencia chama o turno do oponente
        :pram Opponent proximo jogador
        """
        if self.GetStamina() >= 1:  # maior que pq caso seja um volor entre zero e um, não cobre o custo de um atk fraco

            ChangeColor()  # funcao qeu muda cor do codigo. Ignora isso
            self.IncreaseStamina()  # funcao qeu encrementa Stamina
            self.Logs(Opponent)  # essa função aqui e so pra não deixar um monte de print poluindo o codigo

            print('1 - Descanso Curto')
            print('2 - Ataque ')
            op = int(input("Escolha : "))

            if op == 1:  # se o usuario escolher a o descanço, a funcao de descanso e chamada
                self.ShortRest()

            elif op == 2:  # se escolher o ataque, a função de ataque, tabem devera escolher o tipo de ataque
                print('\t' + '-' * 30)
                print('\tEscolha seu tipo e Ataque'.center(30))
                print('\t' + '-' * 30)
                print('\t1 - Ataque Fraco')
                print('\t2 - Ataque Medio')
                print('\t3 - Ataque Forte')
                opAtk = int(input('\tEscolha : '))
                if (1 <= opAtk <= 3) and self.__Stamina >= float(opAtk):  # entao a função de ataque e chamada
                    self.Attack(Opponent, opAtk)
                else:
                    print('\n\t~~Ataque invaliddo~~')
            else:
                print('~~Escolha invalida~~')

            print(f'Fim do turno de {self.playerName}')

        if self.GetLife() > 0 and Opponent.GetLife() > 0:  # se a vida de ambos os jogadores ainda e maior que 0
            Opponent.Turn(self)  # então chama o turno do proximo jogador

    # metodos Chamados dentro do metodo

    def IncreaseStamina(self):
        """Chamado no inicio do turno para aumentar a stamina e checar se e maior que 8"""
        if self.__Stamina < 8:  # checa se a stamina e maior que 8 antes de adicionar
            self.__Stamina += 1 + (self.__Attributes['agility'] * 0.15)
            if self.__Stamina > 8:  # checa se apos a adicao o valor da stamina e maior qeu 8
                self.__Stamina -= (self.__Stamina - 8)  # caso seja, diminui a diferença

    def Logs(self, Opponent):  # so botei os prints do começo do turno aqui dentro pra não poluir na hora de ler
        """
        Exibe um relatorio no terminal contedo as informações basicas de ambos os jogadores
        :param Opponent Jogador inimigo
        """
        global RegisterName

        print('-=' * 15)
        print(f'Turno De {self.playerName}'.center(30))
        print('-=' * 15 + '\n')

        print('-' * 30)
        print(f'{self.playerName}'.center(30))
        print('-' * 30)
        print(f'\tStamina : {round(self.GetStamina(), 2)}')
        print(f'\tVida : {round(self.GetLife(), 2)}')

        print('=' * 30)

        print(f'{Opponent.playerName}'.center(30))
        print('-' * 30)
        print(f'\tStamina : {round(Opponent.GetStamina(),2)}')
        print(f'\tVida : {round(Opponent.GetLife(),2)}')
        print('-' * 30 + '\n')

        # Daqui pra baixo chama uma funçao qeu salva em um aquivo de texto tudo qeu da sendo printado no terminal

        WriteInFile(RegisterName, '--' * 25 + '\n')
        WriteInFile(RegisterName, f'Turno De {self.playerName} \n')
        WriteInFile(RegisterName, '--' * 25 + '\n\n')

        WriteInFile(RegisterName, f'--{self.playerName}\n')
        WriteInFile(RegisterName, f'\tStamina : {round(self.GetStamina(), 2)}\n')
        WriteInFile(RegisterName, f'\tVida : {round(self.GetLife(), 2)}\n\n')

        WriteInFile(RegisterName, f'--{Opponent.playerName}\n')
        WriteInFile(RegisterName, f'\tStamina : {round(Opponent.GetStamina(),2)}\n')
        WriteInFile(RegisterName, f'\tVida : {round(Opponent.GetLife(),2)}\n')
        WriteInFile(RegisterName, '-' * 50 + '\n\n')

    def ShortRest(self):
        """Chamada quando o jogador escolhe descansar ao invez de atacar"""
        self.__Stamina += 1 + (self.__Attributes['agility'] / 2)  # adiciona mais 1 e a metado que voce tem de agility

    def Attack(self, Opponent, opAtk):
        """
        Ataca o oponete, desconta stamina do atacante e life do inimigo
        :param Opponent: Jogador Alvo
        :param opAtk: tipo de Ataque (fraco 1, medio 2, forte 3)
        """
        self.__Stamina -= opAtk  # diminui a stamina que e equivalente a opção de atk
        print(f'Stamina {self.playerName}: {self.GetStamina()}')
        WriteInFile(RegisterName, f'Stamina {self.playerName}: {self.GetStamina()} \n')

        self.IncreaseCritical(opAtk)
        print(f'Critico {self.playerName} : {self.GetCritical()}\n\n')
        WriteInFile(RegisterName, f'Critico {self.playerName} : {self.GetCritical()}\n\n')

        if self.FailChance():
            damage = self.Damage(self.__Attributes['attack'], Opponent.GetAttribute('defense'), opAtk)
            Opponent.SetLife(Opponent.GetLife() - damage)

    def IncreaseCritical(self, opAtk):
        """
        Chamada durante o ataque para acrecentar pontos a Barra de critico
        :param opAtk: tipo de Ataque (fraco 1, medio 2, forte 3)
        """
        if self.GetCritical() < 100:
            porcent_opAtk = opAtk * 10
            porcent_Brutality = self.__Attributes['brutality'] * 0.2
            porcent_Increase = porcent_opAtk + (porcent_opAtk * porcent_Brutality)
            self.SetCritical(porcent_Increase + self.GetCritical())

    def FailChance(self):
        """
        Calcula a chance de falhar do Atacante, de acordo com sua Barra de Critico
        """
        if self.GetCritical() < 100:
            difficulty = 50 - (self.__Attributes['brutality'] * 10)
            RandNum = randint(1, 100)

            if RandNum >= difficulty:
                return True
            else:
                return False
        else:
            return True

    def Damage(self, Atk, Def, opAtk):  # função pra calcular o dano
        """
        Calcula o dano e acrecenta o bonus de Critico caso haja
        :param Atk: Valor de Attack do tacante
        :param Def: Valor de Defense do Defensor
        :param opAtk: tipo de Ataque (fraco 1, medio 2, forte 3)
        """
        global RegisterName
        opDamage = 1 + ((opAtk + 1) / 10)

        if Atk == 1:  # identificar opção de atk
            baseDamage = randint(13, 18)
        elif Atk == 2:
            baseDamage = randint(19, 25)
        elif Atk == 3:
            baseDamage = randint(26, 35)
        ''' 
        dano recebe o calculo de dano (base * op) vezes a porcentagem da defesa
        (1 - (Def * 0.15)) o menos cem e pra ele ja calcular a porcentagem final
        '''
        valueDef = 100 - (Def * 15)  # calculo somente da porcentagem de def, unicamente pra poder printar
        damage = ((baseDamage * opDamage) * (1 - (Def * 0.15)))  # calculo do do dano incluido a equação da defesa

        if self.GetCritical() >= 100:
            if opAtk == 2 or opAtk == 3:
                damage *= 2
                self.SetCritical(0)

        print('-' * 30)
        print(f'porcentagem de Atk que passa pela defesa: {valueDef}%')
        print(f'DanoFinal : {damage}')
        print('-' * 30)

        WriteInFile(RegisterName, '-' * 30 + '\n')
        WriteInFile(RegisterName, f'porcentagem de Atk que passa pela defesa: {valueDef}%' + '\n')
        WriteInFile(RegisterName, f'DanoFinal : {damage}' + '\n')
        WriteInFile(RegisterName, '-' * 30 + '\n')

        return damage

    def RegisterPlayer(self):
        """
        Registra todos os atributos do player em um arquivo de texto
        :return: sem retorno
        """
        global RegisterName

        WriteInFile(RegisterName, '--' + self.playerName.upper() + '\n')
        for key, value in self.__Attributes.items():
            WriteInFile(RegisterName, f'{key} : {value}' + '\n')
        WriteInFile(RegisterName, '-'*50 + '\n')
        WriteInFile(RegisterName, 'BARRAS\n')
        WriteInFile(RegisterName, '-'*50 + '\n')
        WriteInFile(RegisterName, 'Life : ' + str(self.__Life) + '\n')
        WriteInFile(RegisterName, 'Stamina : ' + str(self.__Stamina) + '\n')
        WriteInFile(RegisterName, 'Critical : ' + str(self.__Critical) + '\n')
        WriteInFile(RegisterName, 'Crystal : ' + str(self.__Crystal) + '\n\n')
