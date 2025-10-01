from django.forms import ModelForm
from main.models import News
from django.utils.html import strip_tags

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category", "thumbnail", "is_featured"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)


# model = News untuk menunjukkan model yang akan digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek News.
# fields = ["title", "content", "category", "thumbnail", "is_featured"] untuk menunjukkan field dari model News yang digunakan untuk form. Field created_at dan news_views tidak dimasukkan ke list fields karena ditambahkan secara otomatis.