from hazm import word_tokenize, Normalizer, stopwords_list
from collections import Counter, defaultdict

# خواندن متن از فایل
with open("./exercise2/text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# نرمال‌سازی و توکنایز کردن متن
normalizer = Normalizer()
tokens = word_tokenize(normalizer.normalize(text))

# حذف کلمات توقف
stop_words = set(stopwords_list())
filtered_tokens = [word for word in tokens if word not in stop_words]

# ایندکس‌گذاری کلمات
token_index = defaultdict(list)
for index, word in enumerate(tokens):
    if word not in stop_words:
        token_index[word].append(index)

# شمارش و مرتب‌سازی کلمات
word_counts = Counter(filtered_tokens)
sorted_word_counts = word_counts.most_common()

# نمایش نتایج
print("کلمات پردازش‌شده و فراوانی آن‌ها:")
for word, count in sorted_word_counts:
    print(f"{word}: {count}, موقعیت‌ها: {token_index[word]}")
