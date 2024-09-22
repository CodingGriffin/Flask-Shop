from flask import Flask, render_template, abort, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key in production

# Sample product data (updated with placeholder image)
products = [
    {"id": 1, "name": "שמפו מרענן", "price": 49.99, "image": "placeholder.svg", "description": "שמפו מרענן לכל סוגי השיער"},
    {"id": 2, "name": "קרם לחות", "price": 79.99, "image": "placeholder.svg", "description": "קרם לחות עשיר לעור הפנים"},
    {"id": 3, "name": "מסכת שיער", "price": 59.99, "image": "placeholder.svg", "description": "מסכת שיער מזינה לשיער רך ובריא"},
    {"id": 4, "name": "סרום לפנים", "price": 89.99, "image": "placeholder.svg", "description": "סרום מרוכז להזנת העור"},
    {"id": 5, "name": "מברשת שיער", "price": 39.99, "image": "placeholder.svg", "description": "מברשת שיער איכותית לסירוק קל"},
    {"id": 6, "name": "לק ציפורניים", "price": 29.99, "image": "placeholder.svg", "description": "לק ציפורניים באיכות מקצועית"},
    {"id": 7, "name": "קרם ידיים", "price": 19.99, "image": "placeholder.svg", "description": "קרם ידיים מזין ומרכך"},
    {"id": 8, "name": "מסקרה", "price": 69.99, "image": "placeholder.svg", "description": "מסקרה לריסים ארוכים ומלאים"}
]

# Sample blog posts data (updated with placeholder image)
blog_posts = [
    {"id": 1, "title": "טיפים לטיפוח שיער מתולתל", "image": "placeholder.svg", "excerpt": "גלו את הסודות לשמירה על תלתלים בריאים ויפים..."},
    {"id": 2, "title": "מדריך לבחירת פאה מושלמת", "image": "placeholder.svg", "excerpt": "כל מה שצריך לדעת לפני רכישת פאה חדשה..."},
    {"id": 3, "title": "טרנדים חמים בעיצוב שיער", "image": "placeholder.svg", "excerpt": "הכירו את הסגנונות החמים ביותר לעונה הקרובה..."}
]

@app.route("/")
def index():
    featured_products = products[:4]  # Display the first 4 products as featured
    latest_blog_posts = blog_posts[:3]  # Display the latest 3 blog posts
    return render_template("index.html", featured_products=featured_products, latest_blog_posts=latest_blog_posts)

@app.route("/products")
def product_listing():
    return render_template("products.html", products=products)

@app.route("/product/<int:product_id>")
def product_details(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        abort(404)
    return render_template("product_details.html", product=product)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Here you would typically save the contact form data or send an email
    # For now, we'll just flash a success message
    flash("תודה על פנייתך! נחזור אליך בהקדם.", "success")
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", blog_posts=blog_posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
