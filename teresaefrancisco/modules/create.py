import os
import unidecode

from flask import Blueprint, flash, g, redirect, render_template, request, url_for , current_app
from werkzeug.security import check_password_hash, generate_password_hash
from teresaefrancisco.tools import tools

from teresaefrancisco.models import Product , ProductImage

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route('/product', methods=('GET', 'POST'))
def product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = float(request.form.get('price')) if request.form.get('price') else None
        store = request.form.get('store')
        for_honeymoon = True if request.form.get('for_honeymoon') else False

        product = Product(name=name,price=price)
        if description:
            product.store = description
        if store:
            product.store = store
        if for_honeymoon:
            product.for_honeymoon = for_honeymoon
        product.create()

        files = request.files.getlist('pictures')

        for index in range(len(files)):
            file = files[index]
            if file.filename != '':
                image_name = str(product.name).replace(" ", "").lower()
                image_name = unidecode.unidecode(image_name)

                filename = os.path.join('images','products','{image_name}{index}.jpg'.format(image_name=image_name,index=index))
                path = current_app.root_path + url_for('static', filename = filename)
                file_exists = os.path.exists(path)
                if not file_exists:
                    img_file = open(path,'wb')
                    img_file.close()
                file.save(path)

                new_image = ProductImage(path=filename)

                new_image.product = product
                new_image.create()
        return redirect(url_for('edit.products'))


    return render_template('create/product.html')