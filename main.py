aluno = dict()

while True:
    print('-=' *30)
    aluno['nome'] = str(input("Nome: "))
    aluno['nota1'] = float(input("1º nota: "))
    aluno['nota2'] = float(input("2º nota: "))
    media = (aluno['nota1'] + aluno['nota2'])/2
    aluno['media'] = media
    print('-='*30)
    print(f"- {aluno['nome']} obteve a média de {media}")
    if media < 5:
        print("- Sua situação acadêmica é: Reprovado")
    else:
        print("- Sua situação acadêmica é: Aprovado")
    while True:
        resp = str(input('Desejas verificar a situação de outro discente? Digite [S/N]'))
        if resp in 'Nn' or resp in 'Ss':
            break
        else:
            print('Comando Invalido!')
            continue
    if resp in 'Ss':
        continue
    else:
        break

print('programa finalizado')