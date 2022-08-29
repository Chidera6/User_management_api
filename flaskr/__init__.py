from hashlib import new
import os
import json
import requests
from flask import Flask,jsonify,abort,request
from models import setup_db, Country,User,db

"""
country_per_page = 10

def paginate_country(request,):
  page = request.args.get("page", 1, type=int)
  start = (page - 1) * country_per_page
  end = start + country_per_page
  current_country = countrys[start:end]
  return current_country
"""
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    
    """
    @app.route("/")
    def home():
        return 'stella'
    
    

    #Populate the countries table by getting the countries data from the external api store it in a variable called response.Then convert this variable to text and store it in new_data.
    #convert it to json format and store in a variable called data,loop through the keys in the variable data from the data and finally loop through the looping variable obtained from the first loop.
    #Assign this Finally print poplatio completed on sucessful insert.
    
    response = requests.get('https://countriesnow.space/api/v0.1/countries/codes')
    new_data = response.text
    data = json.loads(new_data)
    new_country = data['data']
    for country in new_country:
        country_table = Country(
        country_code = country['code'],
        country_name = country['name'],
        short_code = country['dial_code']         
        )
        db.session.add(country_table)
        db.session.commit()
    print('population completed')
    """

    @app.route("/create", methods=['POST'])
    def post_user():
        user_country = request.form.get('country_name')
        country = Country.query.filter(Country.country_name == user_country).first()
        if country:
            firstName = request.form.get("first_name")
            lastName = request.form.get("last_name")
            email  = request.form.get("email")
            phone = request.form.get("phone")
            sex = request.form.get("sex")
            try:
                x = User(first_name=firstName,last_name=lastName,email=email,phone=phone,status=True,sex=sex,country_id=country.id)
                db.session.add(x)
                db.session.commit()
                return jsonify({
                    "User_country": x.country.country_name,
                    "User_created": x.last_name + " " + x.first_name,
                    "Success":True,
                    }),200
            except Exception:
                abort(400)      
        
        

    @app.route('/users')
    def get_user():
        users = User.query.all()
        try:
            all_users = []
            for user in users:
                new_user = {'country_id':user.country_id,'uuid':user.user_id,'id':user.id,'first_name':user.first_name,'last_name':user.last_name,'email':user.email,'phone':user.phone,'sex':user.sex,'status':user.status,'created_at':user.created_at}
                all_users.append(new_user)
                return jsonify({
                    'success':True,
                    'users':all_users
                    }),200
        except Exception:
            abort(422)

    @app.route('/users/<int:user_id>')
    def get_user_by_id(user_id):
        x = User.query.get_or_404(user_id)
        try:
            return jsonify({
                "success": True,
                "user_id": x.id,
                "user_name":x.first_name + " " + x.last_name,
                }),200
        except Exception:
            abort(422)

    @app.route('/users/<int:user_id>', methods=['PATCH'])
    def update_user(user_id):
        new_user = User.query.filter_by(user_id=user_id)
        new_user.first_name = request.form.get("first_name")
        new_user.last_name = request.form.get("last_name")
        new_user.email  = request.form.get("email")
        new_user.phone = request.form.get("phone")
        new_user.sex = request.form.get("sex")
        try:
            db.session.commit()
            return jsonify({
                "success": True,
                "updated":user_id,
                }),200
        except Exception:
            abort(400)

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user_by_id(user_id):
        try:
            user = User.query.get_or_404(user_id)
            db.session.delete(user)
            db.session.commit()
            return jsonify({
                "success": True, 
                "deleted": user.user_id
                }),200
        except Exception:
            abort(404)


    @app.route("/activate/<int:user_id>")
    def activate_user(user_id):
        try:
            user = User.query.get_or_404(user_id)
            user.status = True
            return jsonify({
                "success":True
                }),200
        except Exception:
            abort(422)


    @app.route("/deactivate/<int:user_id>")
    def deactivate_user(user_id):
        try:
            user = User.query.get_or_404(user_id)
            user.status = False
            return jsonify({
                "success":True
                }),200
        except Exception:
            abort(422)


    @app.route("/countries")
    def get_countries():
        x = Country.query.all()
        try:
            all_country = []
            for country in x:
                new_country = {'id':country.id,'country_name':country.country_name,'country_code':country.country_code,'short_code':country.short_code}
                all_country.append(new_country)
                return jsonify({
                    "success":True,
                    "list_of_countries": all_country
                    }),200
        except Exception:
            abort(422)

    return app