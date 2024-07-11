'''
# ENCONTRANDO CONECTORES CHAVES

users = [{"id": 0, "name": "Vitor"},
         {"id": 1, "name": "Ana"},
         {"id": 2, "name": "Fabiane"},
         {"id": 3, "name": "Douglas"}]

friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3)]

friendships = {user["id"]: [] for user in users} # user assume o que tem no users a cada interação, por isso o user["id"] é de facil acesso ao user, por ele "ser" dele

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


# Definir agora qual o número médio de concexões

def number_of_friends(user): #parâmetro user é um dictionary, um "clone" de users
    user_id = user["id"]
    friend_ids = friendships[user_id] # acessa o valor do id especificado
    return len(friend_ids)

total_conections = sum(number_of_friends(user) for user in users)
print(total_conections) # 10

num_users = len(users) # tamanho da lista de usuários
avg_connections = total_conections / num_users 
print(avg_connections)

# Encontrar a pessoa com mais conexões

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users] # nessa linha de código ele armazena em uma tupla o user_id e a quantidade de conexões a cada interação dentro de uma lista.

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse = True) #id_and_friends "assume" o num_friends_by_id e id_and_friends[1] retorna o segundo valor da tupla
print(num_friends_by_id) # retorno dele é (id,amigos)
'''

# CIENTISTAS DE DADOS QUE TALVEZ VOCÊ CONHEÇA