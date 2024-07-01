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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style type="text/css">
        nav {
            background-color: beige;
            display: flex;
            justify-content: space-between;
            align-items: center;
            overflow: hidden;
            padding: 0 10px;
        }

        .nav-left {
            font-size: 17px;
            color: black;
            text-decoration: underline pink 20%;
        }

        .nav-right {
            display: flex;
        }

        nav a.active {
            background-color: beige;
            color: black;
        }
        
        .nav-right a {
            display: block;
            padding: 14px 16px;
            text-decoration: none;
            color: black;
            text-align: center;
            font-size: 17px;
            text-shadow: 2px 2px pink;
        }

        @media (max-width: 800px) {
            .nav-right a:not(:first-child) {
                display: none;
            }
            .nav-right a.icon {
                float: right;
                display: block;
            }
        }

        @media (max-width: 600px) {
            .nav-right.responsive {
                position: relative;
            }
            .nav-right.responsive a.icon {
                position: absolute;
                right: 0;
                top: 0;
            }
            .nav-right.responsive a {
                float: none;
                display: block;
                text-align: right;
            }
        }

        /* Slideshow container */
        .slideshow-container {
            position: relative;
            max-width: 1000px;
            margin: auto;
        }

        .mySlideshows {
            display: none;
        }

        .fade {
            animation-name: fade;
            animation-duration: 1.5s;
        }

        @keyframes fade {
            from {opacity: .4} 
            to {opacity: 1}
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            padding: 16px;
            margin-top: -22px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            border-radius: 0 3px 3px 0;
            user-select: none;
        }

        .next {
            right: 0;
            border-radius: 3px 0 0 3px;
        }

        .prev:hover, .next:hover {
            background-color: rgba(0,0,0,0.8);
        }


        .text {
            color: pink;
            font-size: 35px;
            padding: 50px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
        }

        .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active, .dot:hover {
            background-color: #717171;
        }

       #myTop {
            display: none; /* Hidden by default */
            position: fixed; /* Fixed position */
            bottom: 20px; /* Place the button at the bottom of the page */
            right: 30px; /* Place the button 30px from the right */
            z-index: 99; /* Make sure it does not overlap */
            border: none; /* Remove borders */
            outline: none; /* Remove outline */
            background-color: pink; /* Set a background color */
            color: black; /* Text color */
            cursor: pointer; /* Add a mouse pointer on hover */
            padding: 15px; /* Some padding */
            border-radius: 25px; /* Rounded corners */
            font-size: 18px; /* Increase font size */
        }

        #myTop:hover {
            background-color: beige; /* Add a dark-grey background on hover */
        }

        footer {
            padding: 5px;
            text-align: center;
            background-color:beige;
        }

        footer a{
            padding: 10px;
            text-align: center;
            text-decoration: none;
            font-size: 25px;
        }

        footer a:hover {
            color: pink;
        }

        .row {
            display: flex;
            flex-wrap: wrap;
            align-items: stretch;
        }

        .colum {
            padding: 10px;
        }

        .colum.side {
            flex: 1;
            padding: 10px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        .colum.middle {
            flex: 1;
            padding: 10px;
            margin-bottom: 10px;
            overflow: hidden;
        }
    </style>
</head>

<body>
    <button onclick="topFunction()" id="myTop" title="Go to top">Top</button>

    <script>
        // Get the button
        var mybutton = document.getElementById("myTop");

        // When the user scrolls down 20px from the top of the document, show the button
        window.onscroll = function() {
            scrollFunction();
        };

        function scrollFunction() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                mybutton.style.display = "block";
            } else {
                mybutton.style.display = "none";
            }
        }

        // When the user clicks on the button, scroll to the top of the document
        function topFunction() {
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
        }
    </script>
    <nav id="myTopnav" class="topnav">
        <div class="nav-left">T AND Q LOVE</div>
        <div class="nav-right" id="nav-right">
            <a href="/" class="active">首頁</a>
            <a href="/photo2">照片牆2</a>
            <a href="/photo3">週年照片牆</a>
            <a href="/play">澎湖一日遊</a>
            <a href="javascript:void(0);" class="icon" onclick="navFunction()">&#9776;</a>
        </div>
    </nav>

       <header class="slideshow-container">
        <div class="mySlideshows fade">
            <img src="static/428.jpg" style="width: 100%;">
            <div class="text">我們的愛情生活 -1</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/112.jpg" style="width: 100%;">
            <div class="text">我們的愛情生活 - 2</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/113.jpg" style="width: 100%;">
            <div class="text">我們的愛情生活 - 3</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/14.jpg" style="width: 100%;">
            <div class="text">我們的愛情生活 - 4</div>
        </div>

        <div class="mySlideshows fade">
            <img src="static/15.jpg" style="width: 100%;">
            <div class="text">我們的愛情生活 - 5</div>
        </div>

        <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
        <a class="next" onclick="plusSlides(1)">&#10095;</a>

        <div style="text-align: center;">
            <span class="dot" onclick="currentSlide(1)"></span>
            <span class="dot" onclick="currentSlide(2)"></span>
            <span class="dot" onclick="currentSlide(3)"></span>
            <span class="dot" onclick="currentSlide(4)"></span>
            <span class="dot" onclick="currentSlide(5)"></span>
        </div>
    </header>

     <script>
        function navFunction() {
            var x = document.getElementById("nav-right");
            if (x.className === "nav-right") {
                x.className += " responsive";
            } else {
                x.className = "nav-right";
            }
        }

        let slideIndex = 1;
        showSlides(slideIndex);

        function plusSlides(n) {
            showSlides(slideIndex += n);
        }

        function currentSlide(n) {
            showSlides(slideIndex = n);
        }

        function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("mySlideshows");
            let dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}
            if (n < 1) {slideIndex = slides.length}
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex-1].style.display = "block";
            dots[slideIndex-1].className += " active";
        }
    </script>
    <main>
        <article>
        <section class="row">
            <div class ="colum side">
                <h3>我們的ig共同帳號</h3>
                
            </div>
                
            <div class ="colum middle">
                <h3>運動紀錄片</h3>
                <p style="color:#f2a30f">下面是我與寶寶一起健身的影片</p>
                
            </div>

            <div class="colum side">
                <h2>健身前後的感受</h2>
                <p style="color:#c16fd1">學員:荃喜寶寶想對教練翔順寶寶說的話:謝謝你對我耐心的訓練以及買奶昔給我增重,寶寶在訓練我時我真的覺得好折磨,畢竟我是個不愛運動的人,但遇到你我慈知道運動的有趣,謝謝你我會努力好好練出我的馬甲線的</p>

                <p style="color:#f2a30f">寶寶想對學員說的話以及教人的心得:</p>
            </div>
        </section>
    </article>
    </main>
    <footer>
        <a href="https://www.instagram.com/tq.__1314/"><i class="fa-brands fa-instagram-square"></i>Ig</a>
        <a href="https://www.youtube.com/embed/IjbA3drystA"><i class="fas fa-play-circle"></i>yt1</a>
        <a href="https://www.youtube.com/embed/hcQH-VKbl58"><i class="fas fa-play-circle"></i>yt2</a>
        <h5>Copyright ©  楊荃喜. 許翔順. All Rights Reserved.</h5>
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


#if __name__ == "__main__":
#  app.run()