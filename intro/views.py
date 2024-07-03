from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
import bs4
import xlsxwriter

from intro.models import Product


# Create your views here.


def index(request):
    return HttpResponse('A mers:)')


def show_name(request):
    return HttpResponse('A mers si a doua oara:)')


@login_required()
def cars(request):
    context = {
        'all_cars': [
            {
                'name': 'Volvo',
                'model': 'XC 60',
                'color': 'White',
                'year': 2024
            },
            {
                'name': 'BMW',
                'model': 'Series 4',
                'color': 'Black',
                'year': 2023
            },
            {
                'name': 'Mercedes',
                'model': 'A-Class',
                'color': 'Silver',
                'year': 2022
            }
        ]
    }
    return render(request, 'intro/list_of_cars.html', context)


@login_required()
def phones(request):
    context = {
        'all_phones': [
            {
                'name': 'Samsung',
                'model': 'S23',
                'color': 'White',
                'year': 2023
            },
            {
                'name': 'iPhone',
                'model': '15',
                'color': 'Black',
                'year': 2023
            },
            {
                'name': 'OnePlus',
                'model': '15T',
                'color': 'Silver',
                'year': 2022
            }
        ]
    }
    return render(request, 'intro/list_of_phones.html', context)







def get_data(request):

    url = 'https://www.emag.ro/laptopuri/c?ref=hp_menu_quick-nav_1_1&type=category'
    result = requests.get(url) # verificata daca linkul este valid
    soup = bs4.BeautifulSoup(result.text, 'lxml') #BS este un pachet python pentru a analiza documente HTML si XML
    context = {
        'data': [

        ]
    }
    cases = soup.find_all('div', class_='card-v2')
    for case in cases:
        product={}

        product_name = case.find('a', class_='card-v2-title semibold mrg-btm-xxs js-product-url')
        product_price = case.find('p', class_='product-new-price')

        if product_name is None:
            product['name'] = 'No data available'
        else:
            product['name'] = product_name.text

        if product_price is None:
            product['price'] = 'No data available'
        else:
            product['price'] = product_price.text

        context['data'].append(product)


    # Generarea unui fisier xlsx

    workbook = xlsxwriter.Workbook('Emag.xlsx') # adaugarea unui excel nou
    worksheet = workbook.add_worksheet('Produse') # adaugarea unui sheet noy in excel

    row = 0
    col = 0
    for prod in context['data']:
        worksheet.write(row, col, prod['name'])
        worksheet.write(row, col + 1, prod['price'])
        row += 1

        # Stocare in tabela intro_product
        Product.objects.create(name=prod['name'], price=prod['price'])
    workbook.close()







    return redirect('home')


