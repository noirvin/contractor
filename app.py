from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from guitars_list import *

client = MongoClient()
db = client.SlapStore
guitars = db.guitars

guitars = db.guitars
comments = db.comments

slap_reviews = Slap_Store(guitars)
slap_reviews.show_guitars()


app = Flask(__name__)






#playlists = [
#    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
#]

@app.route('/')
def guitars_index():

    return render_template('guitars_index.html', guitars=guitars.find())


@app.route('/guitars/<guitar_id>')
def guitars_show(guitar_id):
    """Show a single guitar."""
    guitar = guitars.find_one({'_id': ObjectId(guitar_id)})
    guitar_reviews = guitars.find({'guitar_id': ObjectId(guitar_id)})
    return render_template('guitars_show.html', guitar=guitar, reviews=guitar_reviews)

@app.route('/guitars/<guitar_id>/reviews/<review_id>/edit')
def reviews_edit(review_id):
    """Show the edit form for a review."""
    review = reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('reviews_edit.html', review=review, title='Edit Review')

@app.route('/guitars/reviews/<review_id>', methods=['POST'])
def reviews_save(review_id):
    """Save an edited review."""
    saved_review = {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
    }
    reviews.update_one(
        {'_id': ObjectId(review_id)},
        {'$set': saved_review})
    return redirect(url_for('guitars_show', review_id=review_id))


@app.route('/guitars/<guitar_id>/reviews', methods=['POST'])
def reviews_new():
    """Submit a new review."""
    review = {
        'subject': request.form.get('title'),
        'content': request.form.get('content'),
        'guitar_id': ObjectId(request.form.get('guitar_id'))
    }
    print(comment)
    review_id = reviews.insert_one(review).inserted_id
    return redirect(url_for('guitars_show', guitar_id=request.form.get('guitar_id')))

@app.route('/guitars/guitars/<guitar_id>/reviews/<review_id>/delete', methods=['POST'])
def reviews_delete(review_id):
    """delete a review."""
    review = reviews.find_one({'_id': ObjectId(review_id)})
    reviews.delete_one({'_id': ObjectId(review_id)})
    return redirect(url_for('guitars_show', guitar_id=guitar.get('guitar_id')))



if __name__ == '__main__':
    app.run(debug=True)
