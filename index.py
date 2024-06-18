from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我和翔順寶寶的紀念網站</title>
    <style type="text/css">
        header, footer {
            text-align: center;
            padding: 10pX;
            margin: 10pX;
        }
        header {
            background-image: url("/static/ve.jpg");
            animation: example1;
            animation-duration: 4s;
            animation-iteration-count: 1;
        }

        @keyframes example1 {
            from {
                transform: rotate(-15deg) translateY(-100%);
                opacity: 0;
            }
            to {
                transform: rotate(0deg) translateY(0%);
                opacity: 1;
            }
        }
        
        footer {
           background-image: url("/static/ve.jpg");
        }

        p {
            font-size: 20px;
        }

        h4 {
            border-color: white;
            border-style: solid ;
            border-radius: 12px;
            border-width: 5px;
            background-color: #e4f3fe;
            font-size: 25px;
        }

        h1 {
            text-decoration: underline solid white 30%;
            text-shadow: 2px 2px #e4f3fe;
        }

        .row {
            display: flex;
            flex-wrap: wrap;
            align-items: stretch;
        }

        .colum {
            padding: 12px;
        }

         .colum.side {
            flex: 1;
            background-image: url("/static/le.jpg");
            padding: 10px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        .colum.middle {
            flex: 1;
            background-image: url("/static/le.jpg");
            padding: 10px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        @media(max-width: 600px) {
            .row {
                flex-direction: column;
                -webkit-flex-direction: column;
            }


        @media(max-width: 580px) {
            .row {
                flex-direction: column;
                -webkit-flex-direction: column;
            }

    </style>
</head>


<body>
<header>
    <h1>我和翔順寶寶旅遊和照片網站</h1>
</header>

<main>
    <article>
        <section class="row">
            <div class ="colum side">
                <h4>旅遊</h4>
                <p><a href ="/play" >澎湖一日遊</a></P> 
                <img src = "static/lv.jpg" width ="350"> 
                <iframe src="https://www.youtube.com/embed/t5O51RmCTsg" allowfullscreen width="300" height="350" ></iframe>
            </div>

            <div class="colum middle">
                <h4>照片牆</h4>
                <p><a href ="/photo3">週年照片牆</a></p> 
                <p><a href ="/photo2">照片牆2024</a></p>
                <p><a href ="/test">測試</a></p>  
                <img src = "static/hug.jpg" width ="350"> 
            </div>
        </section>
    </article>
</main>

<footer>
            Copyright ©  楊荃喜. 許翔順. All Rights Reserved.
</footer>
</body>
</html>
"""


@app.route("/")
def index():
    x = html
    return x


@app.route("/photo2")
def photo2():
    return render_template("photo2.html")

@app.route("/play")
def play():
    return render_template("play.html")


@app.route("/photo3")
def photo3():
    return render_template("photo3.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
  app.run()