
import requests
import json
import pandas as pd
import random

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

def criar_perfil_usuario():
    nomes = ["Alice", "Bob", "Carlos", "Diana", "Eva"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Ferreira"]
    interesses = ["Tecnologia", "Esportes", "Moda", "Música", "Viagens"]
    
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    interesse = random.choice(interesses)
    
    return {
        "nome": f"{nome} {sobrenome}",
        "interesse": interesse
    }


def gerar_noticias_personalizadas(usuario):
    interesse = usuario['interesse']
    
    # Solicita ao usuário para inserir uma notícia
    noticia = input(f"Digite uma notícia sobre {interesse} (máximo de 100 caracteres):\n")
    
    if len(noticia) <= 100:
        return {
            "interesse": interesse,
            "noticia": noticia
        }
    else:
        print("A notícia excedeu o limite de 100 caracteres. Tente novamente.")
        return gerar_noticias_personalizadas(usuario)


def atualizar_usuario_com_noticias(usuario):
    noticia = gerar_noticias_personalizadas(usuario)
    usuario['noticias'].append(noticia)
    
    response = requests.put(f"{sdw2023_api_url}/usuarios/{usuario['id']}", json=usuario)
    
    if response.status_code == 200:
        print(f"Notícias atualizadas para {usuario['nome']} com sucesso!")
        return True
    else:
        print(f"Falha ao atualizar notícias para {usuario['nome']}.")
        print(f"Código de resposta: {response.status_code}")
        print(f"Resposta da API: {response.text}")
        return False
        
        usuario.update(criar_perfil_usuario())
        
        success = atualizar_usuario_com_noticias(usuario)
        
        if success:
            print(f"Notícias atualizadas para {usuario['nome']} com sucesso!")
        else:
            print(f"Falha ao atualizar notícias para {usuario['nome']}.")