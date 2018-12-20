from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    favorites = models.ManyToManyField('Article', blank=True, related_name='favored_by', verbose_name='Избранное')
    email = models.EmailField(max_length=50, verbose_name='Почта')

    def __str__(self):
        return "%s. %s %s %s" % (self.pk, self.name, self.surname, self.email)


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=10000, verbose_name='Статья')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='articles', verbose_name='Aвтор')
    created_at = models.DateField(blank=True, verbose_name='Дата создания')



    def __str__(self):
        return "%s. %s от %s" % (self.pk, self.title, self.author)


class Comment(models.Model):
    text = models.TextField(max_length=10000)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.PROTECT, verbose_name='Статья')
    reply_on_comment = models.ForeignKey('self', blank=True, null=True, related_name='comments', on_delete=models.CASCADE, verbose_name='Комментарий')

    def __str__(self):
        return "%s: %s - %s" % (self.article.title, self.user.name, self.text)


class Rating(models.Model):
    RATING_EXCELLENT = 'excellent'
    RATING_GOOD = 'good'
    RATING_SATISFACTORY = 'satisfactory'
    RATING_BAD = 'bad'
    RATING_POOR = 'poor'

    RATING_CHOICES = (
        (RATING_EXCELLENT, 'excellent'),
        (RATING_GOOD, 'good'),
        (RATING_SATISFACTORY, 'satisfactory'),
        (RATING_BAD, 'bad'),
        (RATING_POOR, 'poor')
    )

    user = models.ForeignKey(User, related_name='article_rating', on_delete=models.PROTECT, verbose_name='Пользователь')
    article = models.ForeignKey(Article, related_name='user_rating', on_delete=models.PROTECT, verbose_name='Статья')
    created_at = models.DateField(verbose_name='Дата создания')
    status = models.CharField(max_length=30, choices=RATING_CHOICES, default=RATING_SATISFACTORY, verbose_name='Оценка')
