import os

restaurants = []

def display_app():
    print('''
        System Food
          
        1 - Register restaurant
        2 - List restaurant
        3 - Activate restaurant
        4 - Exit'
        ''')

def terminate_app():
    display_subtitle('Closing the system, thank you!')

def back_to_menu():
    input('\nPress any key to return to the main menu: ')
    main()

def invalid_option():
    print('\nInvalid option')
    back_to_menu()


def activate_restaurant():
    """
    Ativa ou desativa o status de um restaurante no sistema.

    Solicita ao usuário que insira o nome do restaurante cujo status
    deseja ser alterado. Em seguida, verifica se o restaurante está
    na lista de restaurantes registrados. Se estiver, altera o status
    do restaurante de ativado para desativado ou vice-versa. Caso contrário,
    exibe uma mensagem informando que o restaurante não foi encontrado.

    Inputs:
        - Nome do restaurante

    Output:
        - Altera o status do restaurante na lista de restaurantes
    """
    display_subtitle('Change the status of the restaurant')
    name_restaurant = input('Enter the name of the restaurant you want to change the status: ')
    active_restaurant = False
    for restaurant in restaurants: 
        if name_restaurant == restaurant['name']:
             activate_restaurant = True
             restaurant['active'] = not restaurant['active']
             msg_active = f'The restaurant {name_restaurant} has been successfully activated.' if restaurant['active'] else f'The restaurant has been successfully deactivated.' 
             print(msg_active)

    if not activate_restaurant:
         print(f'{name_restaurant} not found')
            
    back_to_menu()
 
def display_subtitle(text):
    os.system('cls')
    custom = '-' * (len(text))
    print(custom)
    print(text)
    print(custom)
    print()

def register_restaurant():
    """
    Registra um novo restaurante no sistema.

    Solicita ao usuário que insira o nome e a categoria do restaurante,
    em seguida, adiciona-o à lista de restaurantes registrados com um status
    inicial de 'Desativado'.

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    """
    display_subtitle('Registration of new restaurants')
    name_restaurant = input('Enter the name of the restaurant to register: ')
    category = input(f'Enter the category of the {name_restaurant.upper()}: ')
    data_restaurants = {'name':name_restaurant,'category':category,'active': False}
    restaurants.append(data_restaurants)
    print(restaurants)
    print(f'The restaurant {name_restaurant.upper()} was successfully registered!')
    back_to_menu()

def list_restaurant():
    """
    Lista os restaurantes registrados no sistema.

    Exibe uma lista formatada dos restaurantes registrados no sistema,
    mostrando o nome, a categoria e o status (ativo ou desativado) de cada um.

    Output:
        - Exibe a lista de restaurantes
    """
    display_subtitle('List of restaurants')
    print(f'{'Restaurant name'.ljust(24)} | {'Category'.ljust(20)} | Status')
    for index, restaurant in enumerate(restaurants, start=1):
        name_restaurant = restaurant['name']
        category = restaurant['category']
        active = 'Activated' if restaurant['active'] else 'Deactivated'
        print(f'{index} - {name_restaurant.ljust(20)} | {category.ljust(20)} | {active}')

    back_to_menu()
     
def choose_option():
        try:
            selected_option = int(input('Choose an option: '))
            match selected_option:
                case 1:
                    register_restaurant()
                case 2:
                    list_restaurant()
                case 3:
                    activate_restaurant()
                case 4:
                    terminate_app()
                case _:
                    invalid_option()
        except:
                    invalid_option()
def main():
    os.system('cls')
    display_app()
    choose_option()

if __name__ == '__main__':
    main()