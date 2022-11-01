from django.shortcuts import render
from .models import Article, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import CommentForm
from django.views.generic.edit import FormMixin


def index(request):
    # create search
    search_query = request.GET.get('search', '')
    # creating filtering by search
    if search_query:
        contact_list = Article.objects.filter(Q(name__icontains=search_query))
    else:
        contact_list = Article.objects.all().order_by('-id')

    # create paginator
    paginator = Paginator(contact_list, 10)  # number of posts for paginator
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'article/index.html', {'page_obj': page_obj})


class ArticleView(FormMixin, DetailView):
    model = Article
    template_name = 'article/article.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('article', kwargs={'pk': self.get_object().id})

    # request post
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # validation form
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


