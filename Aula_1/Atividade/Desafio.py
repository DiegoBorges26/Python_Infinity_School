def obter_resultados():
    resultados = []
    num_equipes = int(input("Quantas equipes estão participando? "))

    for _ in range(num_equipes):
        nome = input("Digite o nome da equipe: ")
        pontuacoes_str = input(f"Digite as pontuações da equipe {nome}, separadas por espaço: ")
        
        
        pontuacoes = list(map(int, pontuacoes_str.split()))
        resultados.append((nome, pontuacoes))
    
    return resultados


def calcular_classificacao(resultados):
   
    medias = []
    for equipe, pontuacoes in resultados:
        media = sum(pontuacoes) / len(pontuacoes)
        medias.append((equipe, media))

    
    medias.sort(key=lambda x: x[1], reverse=True)

    o
    classificacao = medias

    
    print("\nClassificação final das equipes:")
    for equipe, media in classificacao:
        print(f"{equipe}: {media:.2f}")


def main():
    resultados = obter_resultados()
    calcular_classificacao(resultados)


if __name__ == "__main__":
    main()