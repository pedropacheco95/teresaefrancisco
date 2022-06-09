import pandas
import os
import csv

from flask import Blueprint, redirect, url_for 

bp = Blueprint('upload', __name__, url_prefix='/upload')

from teresaefrancisco.models import Product , ProductImage , Contribution

@bp.route("/from_csv", methods =["GET", "POST"])
def from_csv():
    
    products_table = pandas.read_csv('/Users/pedropacheco/Documents/Projetos/teresaefrancisco/teresaefrancisco/teresaefrancisco/static/data/csv/products.csv')
    contributions_table = pandas.read_csv('/Users/pedropacheco/Documents/Projetos/teresaefrancisco/teresaefrancisco/teresaefrancisco/static/data/csv/contribution.csv')
    product_images_table = pandas.read_csv('/Users/pedropacheco/Documents/Projetos/teresaefrancisco/teresaefrancisco/teresaefrancisco/static/data/csv/product_images.csv')

    for index, row in products_table.iterrows():
        if not pandas.isna(row['name']):
            
            name = row['name']
            description = row['description']
            price = float(row['price'])
            price_paid = float(row['price_paid'])
            store = row['store']
            for_honeymoon = bool(row['for_honeymoon'])

            product = Product(name=name,price=price)
            if description:
                product.store = description
            if price_paid:
                product.price_paid = price_paid
            if store:
                product.store = store
            if for_honeymoon:
                product.for_honeymoon = for_honeymoon
            product.create()
    
    for index, row in contributions_table.iterrows():
        if not pandas.isna(row['name']):
            
            name = row['name']
            value_contributed = float(row['value_contributed'])
            message = row['message']
            product_id = int(row['product_id'])

            contribution = Contribution(name=name,value_contributed=value_contributed,product_id=product_id)
            if message:
                contribution.message = message
            contribution.create()

    for index, row in product_images_table.iterrows():
        if not pandas.isna(row['path']):
            
            path = row['path']
            product_id = int(row['product_id'])
            new_image = ProductImage(path=path)

            product = Product.query.filter_by(id=product_id).first()
            new_image.product = product
            new_image.create()

    return redirect(url_for('main.index'))

@bp.route("/to_csv", methods =["GET", "POST"])
def to_csv():
    models = Product.query.first().all_tables_object()
    instances = Product.query.first().get_all_tables()
    for model in models.keys():
        models[model] = models[model].__table__.columns.keys()
    for model in instances.keys():
        instances[model] = instances[model].all()

    values = {}
    for model in models.keys():
        values[model] = []
        for instance in instances[model]:
            instance_values = []
            for field in models[model]:
                instance_values.append(getattr(instance, field))
            values[model].append(instance_values)

    for model in models.keys():
        file = os.path.join('teresaefrancisco/static/data/csv', '%s.csv' % model)
        fields = models[model]
        rows = values[model]

        with open(file, 'w') as f:
            write = csv.writer(f)
            
            write.writerow(fields)
            write.writerows(rows)
    return redirect(url_for('main.index'))

@bp.route("/from_csv_made_from_excel", methods =["GET", "POST"])
def from_csv_made_from_excel():
    
    products_table = pandas.read_csv('/Users/pedropacheco/Documents/Projetos/teresaefrancisco/teresaefrancisco/teresaefrancisco/static/data/products.csv')

    for index, row in products_table.iterrows():
        if not pandas.isna(row['Name']):
            
            name = row['Name']
            description = row['Description']
            price = float(row['Price'])
            store = row['Store']

            product = Product(name=name,price=price)
            if description:
                product.store = description
            if store:
                product.store = store
            product.create()

            images = row['URL'].split(';')
            for image in images:
                new_image = ProductImage(path=image,product_id=product.id)
                new_image.create()


    return redirect(url_for('main.index'))