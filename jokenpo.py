import random

def jogar():
    print("Vamos jogar pedra, papel e tesoura!")
    rodadas = int(input("Quantas rodadas você deseja jogar? "))
    vitorias_jogador = 0
    vitorias_pc = 0

    for rodada in range(1, rodadas + 1):
        print(f"\nRodada {rodada}:")
        print("Escolha uma opção:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        escolha_jogador = None
        
        while escolha_jogador not in [1, 2, 3]:
            escolha_jogador = int(input("O que você escolhe? "))
        
            if escolha_jogador not in [1, 2, 3]:
                print("Escolha inválida.")
        
        opcoes = ["Pedra", "Papel", "Tesoura"]
        escolha_pc = random.randint(1, 3)
        
        print(f"Sua escolha: {opcoes[escolha_jogador-1]}")
        print(f"O computador escolheu: {opcoes[escolha_pc-1]}")
        
        resultado = (escolha_jogador - escolha_pc) % 3
        
        if resultado == 0:
            print("Empate!")
        elif resultado == 1:
            print("Você ganhou!")
            vitorias_jogador += 1
        else:
            print("O computador ganhou!")
            vitorias_pc += 1

    print("\n===== Final =====")
    print(f"Você venceu {vitorias_jogador} rodadas.")
    print(f"O computador venceu {vitorias_pc} rodadas.")

    if vitorias_jogador > vitorias_pc:
        print("Parabéns! Você venceu!")
    elif vitorias_jogador < vitorias_pc:
        print("O computador venceu!")
    else:
        print("Empate!")

    jogar_novamente = input("Deseja jogar novamente? (1 = Sim / 2 = Não): ")
    if jogar_novamente.lower() == "1":
        jogar()

jogar()