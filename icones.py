import os
from PIL import Image, ImageDraw

def criar_icone_padrao(cor_hex, caminho_saida):
    """
    Cria uma imagem de ícone simples (.ico) com base em uma cor hexadecimal.
    Tamanho padrão para múltiplos tamanhos no Windows: 256x256.
    """
    tamanho = (256, 256)
    imagem = Image.new("RGBA", tamanho, (0, 0, 0, 0))
    draw = ImageDraw.Draw(imagem)
    
    # Convertendo cor hex para RGB
    cor_rgb = tuple(int(cor_hex[i:i+2], 16) for i in (1, 3, 5))
    
    # Desenhando uma representação simples de pasta arredondada/estilizada
    # Aba (fundo da pasta)
    draw.rectangle([20, 70, 236, 220], fill=cor_rgb)
    # Detalhe superior (aba da pasta)
    draw.polygon([(20, 70), (90, 70), (110, 40), (20, 40)], fill=cor_rgb)
    
    # Salvando como .ico contendo múltiplos tamanhos recomendados
    imagem.save(caminho_saida, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

def preparar_pasta_icones(diretorio_base):
    pasta_icones = os.path.join(diretorio_base, "icones")
    os.makedirs(pasta_icones, exist_ok=True)
    
    cores = {
        "aberto.ico": "#32A852",
        "andamento.ico": "#2585D8",
        "pausado.ico": "#F28C28",
        "fechado.ico": "#D93636"
    }
    
    for nome_arquivo, cor in cores.items():
        caminho_ico = os.path.join(pasta_icones, nome_arquivo)
        if not os.path.exists(caminho_ico):
            criar_icone_padrao(cor, caminho_ico)
            print(f"Ícone criado com sucesso: {caminho_ico}")
        else:
            print(f"Ícone já existe: {caminho_ico}")

if __name__ == "__main__":
    # Definindo a pasta principal conforme o projeto
    diretorio_principal = r"C:\Users\italo\OneDrive\Documentos\Projetos\Atualização_de_Pastas\Icones"
    preparar_pasta_icones(diretorio_principal)