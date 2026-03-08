from flask import Flask, render_template_string, url_for
import os

app = Flask(__name__)

AFFILIATE_URL = "https://app.monetizze.com.br/r/AKG24444623?u=c&pl=TT167934"

SITE_URL = "https://crypto-masterclass.vercel.app"

TEMPLATE = """
<!doctype html>
<html lang="pt-BR">
<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Curso de Criptomoedas para Iniciantes</title>

<meta name="description" content="Aprenda do zero ao avançado como investir em criptomoedas com segurança e aproveitar as oportunidades do mercado digital.">

<!-- Open Graph -->
<meta property="og:url" content="{{site_url}}">
<meta property="og:type" content="website">
<meta property="og:title" content="Curso de Criptomoedas para Iniciantes">
<meta property="og:description" content="Aprenda do zero ao avançado como lucrar no mercado cripto.">
<meta property="og:image" content="{{preview_image}}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Curso de Criptomoedas para Iniciantes">
<meta name="twitter:description" content="Aprenda do zero ao avançado como lucrar no mercado cripto.">
<meta name="twitter:image" content="{{preview_image}}">

<style>

body{
font-family: Arial, Helvetica, sans-serif;
background: linear-gradient(135deg,#1e3c72,#2a5298);
color:white;
margin:0;
padding:40px;
text-align:center;
}

.container{
max-width:900px;
margin:auto;
}

h1{
font-size:42px;
margin-bottom:20px;
}

.subtitle{
font-size:20px;
margin-bottom:40px;
}

.btn{
display:inline-block;
padding:20px 40px;
font-size:22px;
font-weight:bold;
color:#001f1d;
background:#00e6b0;
border-radius:12px;
text-decoration:none;
transition:0.2s;
}

.btn:hover{
transform:scale(1.05);
}

</style>

</head>

<body>

<div class="container">

<h1>Domine o Mercado de Criptomoedas</h1>

<p class="subtitle">
Aprenda do zero como investir em Bitcoin, Ethereum e outras criptomoedas
com segurança.
</p>

<a href="{{affiliate}}" class="btn" target="_blank">
QUERO COMEÇAR AGORA
</a>

</div>

</body>
</html>
"""


@app.route("/")
def home():

    preview_image = SITE_URL + url_for("static", filename="preview.png")

    return render_template_string(
        TEMPLATE,
        affiliate=AFFILIATE_URL,
        preview_image=preview_image,
        site_url=SITE_URL
    )


@app.route("/health")
def health():
    return "OK",200


if __name__ == "__main__":

    port = int(os.environ.get("PORT",5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )