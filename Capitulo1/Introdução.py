from collections import Counter
from collections import defaultdict

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


# CIENTISTAS DE DADOS QUE TALVEZ VOCÊ CONHEÇA

def foaf_ids_bad(user):
    return [foaf_id 
            for friend_id in friendships[user["id"]] 
            for foaf_id in friendships[friend_id]]

for user in users:
    print(f"Foaf for user {user['name']} ({user['id']}): {foaf_ids_bad(user)}")
    
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(foaf_id # é o que vai receber e armazenar, ultimo elemento a receber alguma coisa // Counter pega o elemento e conta quantas vezes ele apareceu (Exemplo: se o "a" aparece três vezes numa lista, ele faz uma lista de dicionarios [{a:3}] )
                   for friend_id in friendships[user_id]
                   for foaf_id in friendships[friend_id] # sempre ler um for da direita pra esquerda, o da direita vai entregar algo para a esquerda
                   if foaf_id != user_id # Que não seja o "meu" id 
                   and foaf_id not in friendships[user_id]) # E que o id não esteja presente na "minha" lista de amigos

print(friends_of_friends(users[0])) # O retorno dele é: id da pessoa: quantidade de amigos em comum

# Interesses em comum

interests = [(0, "Hadoop"), (0, "Java"), (1, "NoSQL"), (1, "Python"), (2, "Java"), (2, "MongoDB"), (3, "Java"), (3, "R")]

'''
def data_scientists_who_like(target_interest):
    #Encontre os ids dos ususarios com o mesmo interesse
    
    return [user_id for user_id, user_interest in interests
            if user_interest == target_interest]
    
print(data_scientists_who_like("Java"))
'''

# quando há a necessidade de fazer muitas buscas, é melhor construir um índice de interesses para usuario

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests: # o primeiro recebe o primeiro elemento da lista ou tupla, e o segundo recebe o outro valor
    user_ids_by_interest[interest].append(user_id)
    
# Mesma coisa que o codigo acima só que o user_id vai ser a chave.

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
print(user_ids_by_interest)
print(interests_by_user_id)

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]] # Pegou os interesses de um usuario
        for interested_user_id in user_ids_by_interest[interest] # Usou o interesse de um usuario para identificar quem tem os mesmos interesses
        if interested_user_id != user["id"]) # Exclui você
    
for user in users:
    common_interests = most_common_interests_with(user)
    print(f"Most common interests with user {user['name']} ({user['id']}): {common_interests}")
    
# SALÁRIOS E EXPERIÊNCIA