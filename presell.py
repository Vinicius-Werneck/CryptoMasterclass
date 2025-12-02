# presell_criptos.py — versão melhorada e profissional com correção de imagem
from flask import Flask, render_template_string
import os
import base64

app = Flask(__name__)

AFFILIATE_URL = "https://app.monetizze.com.br/r/AKG24444623?u=c&pl=TT167934"

# FUNÇÃO PARA CARREGAR A IMAGEM EM BASE64
def load_logo_as_base64():
    """
    Tenta carregar a imagem logo.png (ou variações) e converter para Base64.
    Retorna a string Base64 ou None se não encontrar.
    """
    # Lista de possíveis nomes de arquivo de imagem
    possible_names = [
        'logo.png', 'Logo.png', 'logo.jpg', 'Logo.jpg', 
        'logo.jpeg', 'Logo.jpeg', 'image.png', 'Image.png',
        'logo.webp', 'Logo.webp'
    ]
    
    for filename in possible_names:
        if os.path.exists(filename):
            try:
                print(f"✅ Encontrada imagem: {filename}")
                with open(filename, 'rb') as image_file:
                    # Converter para base64
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                
                # Determinar o tipo MIME da imagem
                if filename.lower().endswith('.png'):
                    mime_type = 'png'
                elif filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                    mime_type = 'jpeg'
                elif filename.lower().endswith('.webp'):
                    mime_type = 'webp'
                else:
                    mime_type = 'png'
                
                # Retornar string Base64 formatada
                return f"data:image/{mime_type};base64,{encoded_string}"
                
            except Exception as e:
                print(f"⚠️ Erro ao ler {filename}: {e}")
    
    print("⚠️ Nenhuma imagem encontrada. Usando placeholder.")
    return None

# Carregar a imagem uma vez ao iniciar
LOGO_BASE64 = load_logo_as_base64()

# Exibir informações de debug
print("\n" + "="*60)
print("🎯 LANDING PAGE - CURSO DE CRIPTOMOEDAS")
print("="*60)
print(f"🔗 URL do afiliado: {AFFILIATE_URL}")
print(f"🖼️  Logo carregada: {'SIM' if LOGO_BASE64 else 'NÃO'}")
print("📁 Arquivos na pasta atual:")
for f in os.listdir('.'):
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
        size = os.path.getsize(f)
        print(f"   📸 {f} ({size:,} bytes)")
print("="*60 + "\n")

TEMPLATE = """
<!doctype html>
<html lang='pt-BR'>
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <meta name="description" content="Curso completo de criptomoedas para iniciantes. Aprenda a investir com segurança e domine o mercado cripto.">
    <title>Curso de Criptomoedas para Iniciantes | Domine o Mercado Digital</title>
    <style>
        /* FUNDO GRADIENTE AZUL ANIMADO */
        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298, #1c3f77, #0f2a52);
            background-size: 400% 400%;
            animation: gradientMove 15s ease infinite;
            color: #ffffff;
            line-height: 1.6;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .logo-container {
            position: relative;
            margin: 0 auto 30px auto;
            max-width: 500px;
        }
        
        .logo {
            width: 100%;
            max-width: 500px;
            display: block;
            border-radius: 16px;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeInUp 1.2s ease forwards 0.3s;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            border: 2px solid #00e6b0;
        }
        
        .logo-placeholder {
            width: 100%;
            padding: 60px 20px;
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.8), rgba(0, 230, 176, 0.3));
            border-radius: 16px;
            text-align: center;
            border: 2px dashed #00e6b0;
        }
        
        .logo-placeholder h3 {
            color: #00e6b0;
            margin-bottom: 10px;
        }
        
        .logo-placeholder p {
            color: #c3d9ff;
            font-size: 0.9rem;
        }
        
        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        h1 {
            font-size: 3.2rem;
            margin: 20px 0;
            font-weight: 800;
            background: linear-gradient(45deg, #ffffff, #a8d8ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            opacity: 0;
            animation: fadeInUp 1s ease forwards 0.6s;
        }
        
        .subtitle {
            font-size: 1.4rem;
            color: #c3d9ff;
            margin-bottom: 30px;
            opacity: 0;
            animation: fadeInUp 1s ease forwards 0.9s;
        }
        
        .hero-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
            margin-bottom: 60px;
        }
        
        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin: 40px 0;
        }
        
        .benefit-card {
            background: rgba(255, 255, 255, 0.08);
            padding: 25px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, background 0.3s ease;
        }
        
        .benefit-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.12);
        }
        
        .benefit-card h3 {
            color: #00e6b0;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }
        
        .cta-section {
            text-align: center;
            background: rgba(255, 255, 255, 0.05);
            padding: 50px;
            border-radius: 20px;
            margin: 60px 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .price {
            font-size: 3rem;
            font-weight: 800;
            color: #00e6b0;
            margin: 20px 0;
        }
        
        .old-price {
            text-decoration: line-through;
            color: #ff6b6b;
            font-size: 1.5rem;
        }
        
        .btn {
            display: inline-block;
            margin: 25px 10px;
            padding: 20px 45px;
            font-size: 1.3rem;
            font-weight: 700;
            color: #001f1d;
            background: linear-gradient(45deg, #00e6b0, #00c9ff);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(0, 230, 176, 0.3);
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(0, 230, 176, 0.5);
        }
        
        .btn-secondary {
            background: linear-gradient(45deg, #667eea, #764ba2);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }
        
        .float-btn {
            position: fixed;
            bottom: 25px;
            right: 25px;
            background: linear-gradient(45deg, #00e6b0, #00c9ff);
            color: #001f1d;
            padding: 20px 35px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 800;
            text-decoration: none;
            z-index: 1000;
            box-shadow: 0 10px 30px rgba(0, 230, 176, 0.4);
            animation: pulse 2s infinite ease-in-out, bounce 3s infinite ease-in-out;
            transition: all 0.3s ease;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        
        .float-btn:hover {
            transform: scale(1.1);
        }
        
        .urgency-banner {
            background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: 700;
            border-radius: 10px;
            margin: 30px 0;
            animation: blink 2s infinite;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.8; }
        }
        
        .timer {
            font-size: 2.5rem;
            font-weight: 800;
            color: #ffd700;
            margin: 20px 0;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        }
        
        .testimonial {
            background: rgba(255, 255, 255, 0.05);
            padding: 30px;
            border-radius: 16px;
            margin: 30px 0;
            border-left: 4px solid #00e6b0;
        }
        
        .testimonial-author {
            font-weight: 700;
            color: #00e6b0;
            margin-top: 15px;
        }
        
        @media (max-width: 768px) {
            .hero-section {
                grid-template-columns: 1fr;
                gap: 30px;
            }
            
            h1 {
                font-size: 2.2rem;
            }
            
            .subtitle {
                font-size: 1.1rem;
            }
            
            .btn {
                padding: 18px 35px;
                font-size: 1.1rem;
                display: block;
                margin: 15px 0;
            }
            
            .float-btn {
                bottom: 15px;
                right: 15px;
                padding: 16px 25px;
                font-size: 1rem;
            }
            
            .timer {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class='container'>
        <header class='header'>
            <div class='logo-container'>
                {% if logo_base64 %}
                <img src='{{logo_base64}}' alt='Curso de Criptomoedas' class='logo'
                     onload="console.log('✅ Logo carregada com sucesso!')"
                     onerror="console.log('❌ Erro ao carregar logo'); this.style.display='none';">
                {% else %}
                <div class='logo-placeholder'>
                    <h3>💰 CURSO DE CRIPTOMOEDAS</h3>
                    <p>Domine o Mercado Digital</p>
                    <p style="font-size: 0.8rem; margin-top: 10px; color: #ffd700;">
                        ⚠️ Coloque um arquivo "logo.png" na pasta do script
                    </p>
                </div>
                {% endif %}
            </div>
            
            <h1>Domine o Mercado de Criptomoedas</h1>
            <p class='subtitle'>Aprenda do zero ao avançado como investir com segurança e maximizar seus lucros no universo cripto</p>
        </header>

        <div class='urgency-banner'>
            🚀 OFERTA ESPECIAL: Últimas vagas com desconto! 🚀
        </div>

        <section class='hero-section'>
            <div>
                <h2 style="font-size: 2.2rem; margin-bottom: 20px; color: #00e6b0;">Transforme Seu Conhecimento em Resultados</h2>
                <p style="font-size: 1.2rem; margin-bottom: 25px;">Você já se sentiu perdido no mundo das criptomoedas? Não sabe por onde começar ou tem medo de fazer investimentos errados?</p>
                <p style="font-size: 1.2rem; margin-bottom: 30px;">O curso foi desenvolvido especialmente para iniciantes que querem dominar o mercado cripto de forma segura e lucrativa.</p>
                
                <div style="text-align: center; margin: 40px 0;">
                    <div class='timer'>Tempo Restante: <span id='timer'>15:00</span></div>
                    <div style="color: #ffd700; font-weight: 700; font-size: 1.2rem;">Desconto expira quando o tempo acabar!</div>
                </div>
            </div>
            
            <div style="background: rgba(255, 255, 255, 0.05); padding: 40px; border-radius: 20px; text-align: center;">
                <h3 style="color: #00e6b0; margin-bottom: 25px; font-size: 1.8rem;">OFERTA EXCLUSIVA</h3>
                <div style="margin: 25px 0;">
                    <span class='old-price'>De R$ 198,00</span>
                    <div class='price'>Por apenas R$ 47,00</div>
                </div>
                <p style="margin: 20px 0; color: #c3d9ff;">ou 11x de R$ 5,08</p>
                <a href='{{affiliate}}' class='btn' target='_blank'>QUERO GARANTIR MINHA VAGA</a>
                <p style="margin-top: 20px; font-size: 0.9rem; color: #a8c7fa;">✅ 7 dias de garantia incondicional</p>
            </div>
        </section>

        <section class='benefits-grid'>
            <div class='benefit-card'>
                <h3>📚 Conteúdo Completo</h3>
                <p>Do básico ao avançado: blockchain, wallets, exchanges, estratégias de investimento e análise técnica.</p>
            </div>
            
            <div class='benefit-card'>
                <h3>🛡️ Segurança em 1º Lugar</h3>
                <p>Aprenda a proteger seus investimentos e evitar golpes comuns no mercado cripto.</p>
            </div>
            
            <div class='benefit-card'>
                <h3>🎯 Estratégias Comprovadas</h3>
                <p>Metodologias testadas e aprovadas.</p>
            </div>
            
            <!-- <div class='benefit-card'>
                <h3>💼 Suporte Individual</h3>
                <p>Tire todas suas dúvidas diretamente com nossos especialistas em criptomoedas.</p>
            </div> -->
        </section>

        <section class='cta-section'>
            <h2 style="font-size: 2.5rem; margin-bottom: 20px; color: #00e6b0;">Não Fique Para Trás!</h2>
            <p style="font-size: 1.3rem; margin-bottom: 30px;">O mercado cripto não espera por ninguém. Comece hoje sua jornada rumo à liberdade financeira.</p>
            
            <div style="margin: 40px 0;">
                <a href='{{affiliate}}' class='btn' target='_blank'>GARANTIR VAGA COM DESCONTO</a>
                <a href='{{affiliate}}' class='btn btn-secondary' target='_blank'>VER CONTEÚDO DO CURSO</a>
            </div>
            
            <p style="color: #c3d9ff; font-size: 1.1rem;">⭐ ⭐ ⭐ ⭐ ⭐ 4.9/5 - Mais de 2.300 alunos satisfeitos</p>
        </section>

        <div class='testimonial'>
            <p>"Esse curso mudou completamente minha visão sobre criptomoedas. Em 3 meses já consegui retornar meu investimento e continuo lucrando!"</p>
            <p class='testimonial-author'>- Carlos Silva, Aluno desde 2024</p>
        </div>

        <div class='testimonial'>
            <p>"Finalmente encontrei um curso que explica tudo de forma clara e objetiva. Recomendo para todos que querem começar com o pé direito!"</p>
            <p class='testimonial-author'>- Ana Rodrigues, Investidora Iniciante</p>
        </div>
    </div>

    <a href='{{affiliate}}' class='float-btn' target='_blank'>QUERO COMEÇAR AGORA</a>

    <script>
        // CONTADOR REGRESSIVO MELHORADO
        let time = 900; // 15 minutos
        const timerEl = document.getElementById('timer');
        
        function updateTimer() {
            time--;
            if (time <= 0) {
                timerEl.textContent = "00:00";
                timerEl.style.color = "#ff4747";
                return;
            }
            
            const m = String(Math.floor(time / 60)).padStart(2, '0');
            const s = String(time % 60).padStart(2, '0');
            timerEl.textContent = `${m}:${s}`;
            
            // Efeito visual quando o tempo está acabando
            if (time <= 300) { // 5 minutos
                timerEl.style.color = "#ff6b6b";
                timerEl.style.animation = "blink 1s infinite";
            }
        }
        
        setInterval(updateTimer, 1000);
        
        // ANIMAÇÃO DE DIGITAÇÃO PARA O TÍTULO
        document.addEventListener('DOMContentLoaded', function() {
            const title = "Domine o Mercado de Criptomoedas";
            const titleElement = document.querySelector('h1');
            let i = 0;
            
            function typeWriter() {
                if (i < title.length) {
                    titleElement.innerHTML = title.substring(0, i+1) + '<span style="border-right: 2px solid #00e6b0;">|</span>';
                    i++;
                    setTimeout(typeWriter, 100);
                } else {
                    titleElement.innerHTML = title;
                }
            }
            
            setTimeout(typeWriter, 2000);
        });
        
        // DEBUG NO CONSOLE
        console.log("=== DEBUG DA PÁGINA ===");
        console.log("URL do Afiliado:", "{{affiliate}}");
        console.log("Logo carregada:", {% if logo_base64 %}"SIM"{% else %}"NÃO (usando placeholder)"{% endif %});
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Rota principal da landing page"""
    return render_template_string(
        TEMPLATE, 
        affiliate=AFFILIATE_URL,
        logo_base64=LOGO_BASE64
    )

if __name__ == '__main__':
    print("🌐 Servidor iniciando...")
    print("🔗 Acesse: http://localhost:5000")
    print("🔄 Atualize a página se a imagem não aparecer")
    print("💡 Dica: Certifique-se de que 'logo.png' está na mesma pasta\n")
    
    app.run(debug=True, port=5000)