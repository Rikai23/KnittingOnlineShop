from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Каталог',
        'categories': [
            {'name': 'Игрушки'},
            {'name': 'Сумки'},
            {'name': 'Одежда'},
            {'name': 'Брелки'},
            {'name': 'Распродажа'}
        ],
        'goods': [
            {'image': 'images/bunny_product_1.jpg',
             'name': 'Милый зайчик',
             'description': 'Мягкий и уютный зайка, связанный вручную из гипоаллергенной плюшевой пряжи. Идеальный подарок для детей и милое украшение интерьера.',
             'price': 2000.00},
            {'image': 'images/doll_product_2.jpg',
             'name': "Кукла 'Тильда'",
             'description': 'Очень модна кукла. Вариант подарка для юных принцесс.',
             'price': 3200.00},
            {'image': 'images/labubu_product_3.jpg',
             'name': 'Лабубу',
             'description': 'Этот вязаный Лабубу выполнен вручную в технике амигуруми. Уютный, пушистый и невероятно милый, он легко станет любимым талисманом или украшением комнаты.',
             'price': 3500.00},
        ]

    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context = {
        "name": "Лабубу",
        'description': 'Этот вязаный Лабубу выполнен вручную в технике амигуруми. Уютный, пушистый и невероятно милый, он легко станет любимым талисманом или украшением комнаты.',
        "price": 3500,
        "images": [
            {"url": "images/bunny_product_1.jpg"},
            {"url": "images/doll_product_2.jpg"},
            {"url": "images/labubu_product_3.jpg"},
        ]
    }
    return render(request, 'goods/product.html', context)

