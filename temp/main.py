# calculadora de medias
# desenvolvido por
# Jose Henrique Malta Florian da Silva
# Hincaluan fontes

from temp import Temperatura

def main():
    while True:
        print('''
        Digite a opção desejada:
        1. Converter de Celsius para Fahrenheit
        2. Converter de Fahrenheit para Celsius
        3. Sair
        ''')
        
        escolha = input("Digite 1, 2 ou 3: ")
        
        if escolha == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = Temperatura.celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit}°F")
        elif escolha == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = Temperatura.fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius}°C")
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")

if __name__ == "__main__":
    main()
