from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_wordcloud(combined_column):
    combined_text = " ".join(combined_column)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Most used words in movie content')
    plt.show()
