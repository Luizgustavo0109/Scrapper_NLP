from httpx import get
from parsel import Selector

from csv import DictWriter
import dateparser

def letra(url: str) -> str:
    """Função que retorna a letra da música."""
    response = get(url)
    selec = Selector(text=response.text)
    letra = '\n' .join (selec.css('[data-lyrics-container]::text').getall())
    return letra

def faixas(url: str) -> list[tuple[str, str]]:
    response = get(url)
    selec = Selector(response.text)

    musicas = selec.css('div.chart_row-content')

    return [
        (musica.css('h3::text').get().strip(), musica.css('a').attrib['href'])
        for musica in musicas
    ]


def discos(url: str) -> list[tuple[str | None, ...]]:
    response = get(url)
    s = Selector(response.text)

    discos = s.css('.jsXEqK')

    resultado = []

    for disco in discos:
        disco_url = disco.css('.jsXEqK').attrib['href']
        disco_nome = disco.css('h3.gSnatN::text').get()
        disco_data = disco.css('.ixmAQP::text').get()

        resultado.append(
            (disco_url, disco_nome, disco_data)
        )

    return resultado


url = 'https://genius.com/artists/Matue/albums'


with open('Matue.csv', 'w', newline='', encoding='utf-8') as f:
    writer = DictWriter(f, ['album', 'data', 'musica', 'letra'])
    writer.writeheader()
    for disco in discos(url):
        for faixa in faixas(disco[0]):
            row = {
                'album': disco[1],
                'data': dateparser.parse(disco[2] or ''),
                'musica': faixa[0],
                'letra': letra(faixa[1])
            }
            print(row)
            writer.writerow(row)
    