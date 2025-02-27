from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    template_name = "blogapp/articles_list.html"
    context_object_name = "articles"
    queryset = (
        Article.objects
        .defer("content")
        .select_related("author", "category")
        .prefetch_related("tags")
    )
