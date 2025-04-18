import hashlib

def gerar_hash (senha):
    return hashlib.md5(senha.encode()).hexdigest()

senha = input("Digite sua senha: ")

hash_senha = gerar_hash(senha)
print(f"\nSua senha: '{senha}'")
print(f"\nHash da senha: {hash_senha}")

with open ("hash_senha.txt", "w") as arquivo:
    arquivo.write(hash_senha)
    print(f"\nHash da senha foi salvo em hash_senha.txt")
