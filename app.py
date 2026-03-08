from flask import Flask, render_template_string
import os
import base64

app = Flask(__name__)

AFFILIATE_URL = "https://app.monetizze.com.br/r/AKG24444623?u=c&pl=TT167934"

SITE_URL = "https://crypto-masterclass.vercel.app"
PREVIEW_IMAGE = f"{SITE_URL}/preview.png"


def load_logo_as_base64():
    possible_names = [
        'logo.png','Logo.png','logo.jpg','Logo.jpg',
        'logo.jpeg','Logo.jpeg','image.png','Image.png'
    ]

    for filename in possible_names:
        if os.path.exists(filename):
            try:
                with open(filename, 'rb') as image_file:
                    encoded = base64.b64encode(image_file.read()).decode("utf-8")

                if filename.lower().endswith(".png"):
                    mime = "png"
                else:
                    mime = "jpeg"

                return f"data:image/{mime};base64,{encoded}"

            except:
                pass

    return None


LOGO_BASE64 = load_logo_as_base64()


TEMPLATE = """

<!doctype html>
<html lang='pt-BR'>
<head>

<meta charset='utf-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>

<title>Curso de Criptomoedas para Iniciantes</title>

<meta name="description" content="Aprenda a investir em criptomoedas com segurança e dominar o mercado digital.">

<!-- Open Graph (WhatsApp / Facebook / Telegram) -->
<meta property="og:title" content="Curso de Criptomoedas para Iniciantes">
<meta property="og:description" content="Aprenda do zero ao avançado como lucrar no mercado cripto.">
<meta property="og:image" content="{{preview}}">
<meta property="og:url" content="{{site_url}}">
<meta property="og:type" content="website">

<!-- Twitter / WhatsApp fallback -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Curso de Criptomoedas para Iniciantes">
<meta name="twitter:description" content="Aprenda a investir em criptomoedas com segurança.">
<meta name="twitter:image" content="{{preview}}">

<style>

body{
font-family: Arial;
background:#0f2a52;
color:white;
text-align:center;
padding:40px
}

h1{
font-size:40px
}

.btn{
display:inline-block;
padding:20px 40px;
background:#00e6b0;
color:#001f1d;
font-weight:bold;
text-decoration:none;
border-radius:10px;
margin-top:30px
}

.logo{
max-width:400px;
margin-bottom:30px
}

</style>

</head>

<body>

{% if logo_base64 %}
<img src='{{logo_base64}}' class="logo">
{% endif %}

<h1>Domine o Mercado de Criptomoedas</h1>

<p>
Aprenda do zero como investir em criptomoedas
e começar sua jornada no mercado digital.
</p>

<a href="{{affiliate}}" class="btn" target="_blank">
GARANTIR MINHA VAGA
</a>

</body>
</html>

"""


@app.route('/')
def index():

    return render_template_string(
        TEMPLATE,
        affiliate=AFFILIATE_URL,
        logo_base64=LOGO_BASE64,
        preview=PREVIEW_IMAGE,
        site_url=SITE_URL
    )


@app.route('/health')
def health():
    return "OK",200


if __name__ == '__main__':

    port = int(os.environ.get("PORT",5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )