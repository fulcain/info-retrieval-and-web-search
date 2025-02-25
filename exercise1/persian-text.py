from hazm import word_tokenize, Normalizer, Stemmer, stopwords_list
from collections import Counter

# نمونه متن فارسی
text = "کلاس مبانی بازیابی و اطلاعات - دانشکده علوم انسانی - ساعت ۸"

# نرمال‌سازی متن (تبدیل حروف مختلف به فرمت استاندارد)
normalizer = Normalizer()
normalized_text = normalizer.normalize(text)

# توکنایز کردن متن (شکستن به کلمات)
tokens = word_tokenize(normalized_text)

# حذف کلمات توقف (Stop Words)
stop_words = set(stopwords_list())
filtered_tokens = [word for word in tokens if word not in stop_words]

# ریشه‌یابی (Stemming)
stemmer = Stemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# شمارش تعداد کلمات پردازش‌شده
word_counts = Counter(stemmed_tokens)

# نمایش نتایج
print("کلمات توکن‌شده:", tokens)
print("کلمات بدون استاپ‌ورد:", filtered_tokens)
print("کلمات ریشه‌یابی‌شده:", stemmed_tokens)
print("تعداد کلمات پردازش‌شده:", word_counts)
