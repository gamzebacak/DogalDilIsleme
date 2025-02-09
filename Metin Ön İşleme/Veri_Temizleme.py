# Metinlerdeki fazla boşlukları temizleme

from bs4 import BeautifulSoup
from textblob import TextBlob
import re
import string
text = " Hello,      World,         2035    "
cleaned_text = " ".join(text.split())
print(cleaned_text)


# büyük harf -> küçük harf değişimi

text = "Hello, World,2035"
text1 = text.lower()
print(text1)

# noktalama işaretlerini kaldırma


text = "Hello, World!, 2035"
text2 = text.translate(str.maketrans("", "", string.punctuation))
print(text2)

# özel karakterleri kaldır


text = "Hello, World!, 2035"
text3 = re.sub(r"[^A-Za-z0-9\s]", "", text)
print(text3)

# yazım hatalarının düzeltilmesi

text = "Helıo, Wirld! 2035"
text4 = str(TextBlob(text).correct())
print(text4)

# html ya da url etiketlerini kaldır

html_text = "<div>Hello, World! 2035</div>"
text5 = BeautifulSoup(html_text, "html.parser").get_text()
print(text5)
