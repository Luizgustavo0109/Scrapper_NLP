import matplotlib.pyplot as plt
import polars as pl
import numpy as np

df = pl.read_csv('matue_stats.csv')

#counter = df.group_by('album').len().sort('len')
#fig, ax = plt.subplots()
#ax.set_title('Músicas por Álbum')
#ax.barh(counter['album'], counter['len'], color='skyblue')
#ax.set_yticklabels(counter['album'], rotation=45, ha='right')

#plt.tight_layout()
#plt.show()

for album in df.sort('data').partition_by('album'):
    album = album.sort('tokens')
    mean = album['ttr'].mean()

    n = len(album)
    indices = np.arange(n)
    bar_height = 0.25

    fig, ax = plt.subplots(figsize=(10, n * 0.5))

    bars1 = ax.barh(indices - bar_height, album['tokens'], height=bar_height, label='Tokens (N)', color='skyblue')
    bars2 = ax.barh(indices, album['types'], height=bar_height, label='Types (N)', color='lightgreen')
    bars3 = ax.barh(indices + bar_height, album['ttr'], height=bar_height, label='TTR (%)', color='coral')

    ax.axvline(x=mean, color='gray', linestyle='--', label='Média TTR')

    ax.set_yticks(indices)
    ax.set_yticklabels(album['musica'])

    ax.set_title(f"{album['album'][0]} - {album['data'][0]}")
    ax.set_xlabel('Estatísticas de texto')
    ax.set_ylabel('Nome da música')

    ax.legend()

    plt.tight_layout()
    plt.show()