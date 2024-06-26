from flask import Flask, request, jsonify, render_template, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URI')

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))

class Website(Base):
    __tablename__ = 'websites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False)

def get_websites():
    session = Session()
    websites = session.query(Website).all()
    session.close()
    return websites

def check_website(url):
    try:
        response = requests.get(url)
        response_time = response.elapsed.total_seconds() * 1000
        if response.status_code == 200:
            return {"status": "up", "response_time": response_time}
        else:
            return {"status": "down", "response_time": response_time, "status_code": response.status_code}
    except requests.ConnectionError:
        return {"status": "down", "error": "Failed to establish a connection."}
    except requests.Timeout:
        return {"status": "down", "error": "The request timed out."}
    except requests.RequestException as e:
        return {"status": "down", "error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/websites')
def api_websites():
    websites = get_websites()
    return jsonify([{"id": website.id, "url": website.url} for website in websites])

@app.route('/api/check_status')
def check_status():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is missing"}), 400
    status = check_website(url)
    return jsonify(status)

@app.route('/add_website', methods=['POST'])
def add_website():
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "URL parameter is missing"}), 400
    
    session = Session()
    website = Website(url=url)
    session.add(website)
    session.commit()
    session.close()
    
    return redirect(url_for('index'))

@app.route('/edit_website', methods=['POST'])
def edit_website():
    website_id = request.form.get('id')
    new_url = request.form.get('url')
    if not website_id or not new_url:
        return jsonify({"error": "Missing parameters"}), 400
    
    session = Session()
    website = session.query(Website).filter_by(id=website_id).first()
    if website:
        website.url = new_url
        session.commit()
    session.close()
    
    return redirect(url_for('index'))

@app.route('/delete_website', methods=['POST'])
def delete_website():
    website_id = request.form.get('id')
    if not website_id:
        return jsonify({"error": "ID parameter is missing"}), 400
    
    session = Session()
    website = session.query(Website).filter_by(id=website_id).first()
    if website:
        session.delete(website)
        session.commit()
    session.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
