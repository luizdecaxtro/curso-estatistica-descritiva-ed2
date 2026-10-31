# Gera os MP3 de narração do curso "Estatística Descritiva" com a voz Francisca.
#
# Uso (no seu computador, com internet):
#   pip install edge-tts
#   python gerar_audio.py
#
# O script lê narracao.json e cria um MP3 para cada trecho na pasta "audio":
#   audio/aula00-s0.mp3 ... (aula introdutória)
#   audio/aula01-intro.mp3, audio/aula02-intro.mp3 ... (introdução de cada lição)
# Arquivos que já existem não são refeitos; apague um MP3 para gerá-lo de novo.
#
# Publique a pasta "audio" ao lado dos arquivos aula-NN.html (por exemplo, no GitHub Pages).
# As aulas tocam os MP3 automaticamente e só usam a voz do navegador se um arquivo faltar.

import asyncio
import json
from pathlib import Path

import edge_tts

VOZ = "pt-BR-FranciscaNeural"
VELOCIDADE = "+0%"  # ex.: "-5%" mais devagar, "+5%" mais rápido

PASTA = Path(__file__).parent
SAIDA = PASTA / "audio"


async def main() -> None:
    SAIDA.mkdir(exist_ok=True)
    roteiro = json.loads((PASTA / "narracao.json").read_text(encoding="utf-8"))
    for chave, texto in roteiro.items():
        destino = SAIDA / f"{chave}.mp3"
        if destino.exists():
            print(f"já existe: {destino.name}")
            continue
        await edge_tts.Communicate(texto, VOZ, rate=VELOCIDADE).save(str(destino))
        print(f"gerado: {destino.name}")


if __name__ == "__main__":
    asyncio.run(main())
