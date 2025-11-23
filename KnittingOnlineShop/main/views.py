from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Обрабатывает запросы на главную страницу"""

    # Список текстов, которые будут исп. на главной странице
    texts = [
        {
            "title": "онлайн магазин вязаных изделий",
            "desc": "Каждое изделие создано с теплом и вниманием к деталям. Выберите уникальные вещи, которые подарят уют и подчеркнут вашу индивидуальность."
        }
    ]

    #latest_products = Product.objects.order_by('-id')[:3] #Последнии три товара (для раздела НОВИНКИ)
    #sale_products = Product.objects.filter(is_sale=True)[:3] #Товараы по скидки (отображаем максимум 3шт)

    context = {
        'title': "Вязаные изделия",
        'texts': texts,
    }
    return render(request, 'main/index.html', context)
