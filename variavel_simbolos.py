import random
import time
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_painel(saldo):
    print("=" * 30)
    print("🐯  TIGRINHO PY CASINO  🐯")
    print("=" * 30)
    print(f"💰 Saldo: {saldo}")
    print("=" * 30)

def girar_roleta(simbolos):
    for _ in range(15):
        limpar_tela()
        print("🎰 GIRANDO...\n")
        roleta_temp = [
            random.choice(simbolos),
            random.choice(simbolos),
            random.choice(simbolos)
        ]
        print(" | ".join(roleta_temp))
        time.sleep(0.1)
    return roleta_temp

# ============================
# JOGO
# ============================

simbolos = ["🐯", "🍒", "⭐", "💎", "🍀"]
saldo = 100

while saldo > 0:
    limpar_tela()
    mostrar_painel(saldo)
    input("\nPressione ENTER para girar a roleta...")

    roleta = girar_roleta(simbolos)

    limpar_tela()
    mostrar_painel(saldo)
    print("\nRESULTADO FINAL:")
    print(" | ".join(roleta))

    if roleta[0] == roleta[1] == roleta[2]:
        print("\n🎉 JACKPOT! Você ganhou 50!")
        saldo += 50
    else:
        print("\n❌ Não foi dessa vez! Você perdeu 10.")
        saldo -= 10

    print(f"\n💰 Saldo atual: {saldo}")
    time.sleep(2)

limpar_tela()
print("💀 GAME OVER! Saldo zerado.")
