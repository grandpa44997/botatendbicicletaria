def inicio_atendimento():
    print("Olá! Bem-vindo ao atendimento automatizado da Bicicletaria XYZ.\n")
    print("Por favor, selecione uma das opções abaixo:")
    print("1 - Dúvidas")
    print("2 - Consultas")
    print("3 - Informações")
    print("4 - Sair\n")
    return int(input())

def atendimento_duvidas():
    print("Selecione a categoria de dúvidas:")
    print("1 - Peças")
    print("2 - Manutenção")
    print("3 - Acessórios")
    print("4 - Voltar ao menu anterior\n")
    return int(input())

def atendimento_consultas():
    print("Selecione o tipo de consulta:")
    print("1 - Disponibilidade de peças")
    print("2 - Orçamento de serviços")
    print("3 - Agendamento de serviços")
    print("4 - Voltar ao menu anterior\n")
    return int(input())

def atendimento_informacoes():
    print("Selecione o tipo de informação:")
    print("1 - Endereço e horário de funcionamento")
    print("2 - História da empresa")
    print("3 - Promoções e descontos")
    print("4 - Voltar ao menu anterior\n")
    return int(input())

def resposta_duvidas(opcao):
    if opcao == 1:
        print("Oferecemos uma grande variedade de peças para bicicletas, desde peças para aros e pneus até peças para câmbios e freios.")
    elif opcao == 2:
        print("Oferecemos serviços de manutenção para bicicletas, incluindo regulagem de câmbio, freio e troca de peças.")
    elif opcao == 3:
        print("Temos uma grande variedade de acessórios para bicicletas, incluindo cadeados, cestas, espelhos, luzes, entre outros.")
    elif opcao == 4:
        return False
    return True

def resposta_consultas(opcao):
    if opcao == 1:
        print("Temos diversas peças disponíveis em nosso estoque, por favor entre em contato para verificar a disponibilidade de uma peça específica.")
    elif opcao == 2:
        print("Para realizar um orçamento, por favor entre em contato conosco informando o serviço desejado.")
    elif opcao == 3:
        print("Para agendar um serviço, por favor entre em contato conosco informando a data e hora desejada.")
    elif opcao == 4:
        return False
    return True

def resposta_informacoes(opcao):
    if opcao == 1:
        print("Estamos localizados na Rua das Bicicletas, número 123, e nosso horário de funcionamento é de segunda a sexta das 8h às 18h e aos sábados das 8h às 13h.")
    elif opcao == 2:
        print("A Bicicletaria XYZ foi fundada em 1990 com o objetivo de oferecer aos seus clientes as melhores peças e serviços para bicicletas.")
    elif opcao == 3:
        print("Temos diversas promoções e descontos em nossas peças e serviços, fique atento às nossas redes sociais e site para não perder nenhuma!")
    elif opcao == 4:
        return False
    return True

# Loop principal do sistema de atendimento
while True:
    opcao_selecionada = inicio_atendimento()

    if opcao_selecionada == 1:
        while True:
            opcao_selecionada = atendimento_duvidas()
            if not resposta_duvidas(opcao_selecionada):
                break
    elif opcao_selecionada == 2:
        while True:
            opcao_selecionada = atendimento_consultas()
            if not resposta_consultas(opcao_selecionada):
                break
    elif opcao_selecionada == 3:
        while True:
            opcao_selecionada = atendimento_informacoes()
            if not resposta_informacoes(opcao_selecionada):
                break
    elif opcao_selecionada == 4:
        print("Obrigado por utilizar o atendimento automatizado da Bicicletaria XYZ!")
        break
    else:
        print("Opção inválida, por favor selecione uma opção válida.")

