from wordcloud import WordCloud
import matplotlib.pyplot as plt
import polars as pl
import nltk
import re

from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))
custom_stopwords = {'yeah', 'uh', 'baby', 'lala', 'ai', 'ah', 'ahn', 'ayy', 'oh', 'ill', 'yeyeah', 'mm', 'yeah', 'awwow', 'ahan', 'yeyeahyeyeah'}
stop_words.update(custom_stopwords)

df = pl.read_csv('matue_stats.csv')
wc = WordCloud(width=800, height=800, background_color='white',
               colormap='viridis', max_words=200,
               contour_color='black', contour_width=1)

for album in df.sort('data').partition_by('album'):
    text = ' '.join(album['letra'])
    text = text.replace('\n', ' ')
    text = text.lower()  # lowercase
    text = re.sub(r'[^\w\s]', '', text)  # remove pontuação
    words = text.split()
    
    # Remove stopwords
    filtered_words = [word for word in words if word not in stop_words]
    filtered_text = ' '.join(filtered_words)

    img = wc.generate(filtered_text)

    fig, ax = plt.subplots()
    ax.set_title(album['album'][0])
    ax.imshow(img)
    ax.axis('off')
    plt.show()