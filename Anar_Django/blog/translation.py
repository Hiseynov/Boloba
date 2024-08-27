from modeltranslation.translator import register, TranslationOptions
from .models import Blogs


@register(Blogs)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'desgription')  # Укажите поля, которые хотите перевести


