#-*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect
from flask_images import resized_img_src
from app.blueprints.www.models import Category
from googletrans import Translator
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# Define the blueprint: 'mod_www',
mod_www = Blueprint('mod_www', __name__, template_folder='templates')

category = Category()
translator = Translator()

# Set the route and accepted methods
@mod_www.route('/', methods=['GET'])
def www_index():
	orders = category.load_category(0)
	return render_template("www/index.html", orders = orders)

@mod_www.route('/category/<int:category_id>', methods=['GET'])
def www_category(category_id):
    response = category.load_items_list_all(category_id)
    #if response.itemsList.item.count > 0:
        #for item in response.itemsList.item:
            #item.itemTitle = translator.translate(item.itemTitle.encode('utf-8'), src='pl', dest='sk').text
            #print(translator.translate('DYSZA', src='pl', dest='sk'))

    return render_template("www/index.html", response =
                                                response)

@mod_www.route('/category/<int:category_id>/items', methods=['GET'])
def www_items(category_id):
    orders = category.load_items_list(category_id)
    return render_template("www/index2.html", orders = orders)
