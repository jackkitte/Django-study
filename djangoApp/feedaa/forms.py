from django.forms import Form, CharField, URLField, DateField


class FeedForm(Form):

    title = CharField(max_length=256)
    description = CharField(max_length=1024)
    href = URLField(max_length=2084)


class PageForm(Form):
    
    title = CharField(max_length=256)
    description = CharField(max_length=1024)
    href = URLField(max_length=2084)
    date_published = DateField()
    id = CharField()
