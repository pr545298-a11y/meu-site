from flask import Flask, render_template, request

#
app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    
    link_recebido = request.form.get('link_usuario')
    
   
    print("\n" + "="*40)
    print(f"LINK RECEBIDO COM SUCESSO: {link_recebido}")
    print("="*40 + "\n")
    
    
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Sucesso!</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://i.postimg.cc/jqcJJ0Z4/Whats-App-Image-2026-05-22-at-00-30-43.jpg');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .box-sucesso {{
                background-color: rgba(255, 255, 255, 0.95);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
                text-align: center;
                max-width: 450px;
                width: 90%;
            }}
            h3 {{ color: #28a745; font-size: 24px; margin-bottom: 10px; }}
            p {{ color: #333; word-break: break-all; font-size: 16px; background: #f8f9fa; padding: 10px; border-radius: 5px; }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #007BFF;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                transition: 0.3s;
            }}
            a:hover {{ background-color: #0056b3; }}
        </style>
    </head>
    <body>
        <div class="box-sucesso">
            <h3>✓ Enviado com Sucesso!</h3>
            <p><strong>Link recebido:</strong><br>{link_recebido}</p>
            <a href="/">Enviar outro link</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run