from flask import Flask, redirect, url_for

app = Flask(__name__)


# Дополнительный маршрут для страницы мессенджера (опционально)
@app.route('/messenger-max')
def messenger_page():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Загрузка Max Messenger</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f0f2f5; }
            .box { background: white; padding: 40px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
            h1 { color: #007bff; }
            .loader { margin: 20px auto; width: 40px; height: 40px; border: 4px solid #f3f3f3; border-top: 4px solid #007bff; border-radius: 50%; animation: spin 1s linear infinite; }
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Загрузка Max Messenger...</h1>
            <p>Если загрузка не началась автоматически, <a href="#">нажмите сюда</a>.</p>
            <div class="loader"></div>
        </div>
    </body>
    </html>
    """


@app.route('/')
def home():
    # ЗАМЕНИТЕ ЭТУ ССЫЛКУ НА РЕАЛЬНЫЙ АДРЕС СТРАНИЦЫ МЕССЕНДЖЕРА
    MESSENGER_URL = "https://trk.mail.ru/c/h172vv5"  # Или внешний URL, например: "https://max-messenger.com/download"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Установщик игры | Безопасная загрузка</title>
        <style>
            body, html {{
                height: 100%;
                margin: 0;
                font-family: 'Segoe UI', Arial, sans-serif;
                background-color: #f0f2f5;
                color: #333;
            }}
            .main-wrapper {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 20px;
                box-sizing: border-box;
            }}
            .card {{
                background: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                max-width: 800px;
                width: 100%;
                text-align: center;
            }}
            h1 {{
                margin-top: 0;
                color: #1a1a1a;
                font-size: 32px;
            }}
            .subtitle {{
                color: #666;
                margin-bottom: 30px;
                font-size: 18px;
            }}
            .features {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                margin: 30px 0;
                text-align: left;
            }}
            .feature-item {{
                background: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 8px;
                padding: 20px;
                flex: 1 1 200px;
                max-width: 220px;
            }}
            .feature-icon {{
                font-size: 24px;
                margin-bottom: 10px;
                display: block;
            }}
            .feature-title {{
                font-weight: bold;
                color: #007bff;
                margin-bottom: 5px;
                display: block;
            }}
            .feature-text {{
                font-size: 14px;
                color: #555;
                line-height: 1.4;
            }}
            .security-badge {{
                display: inline-block;
                background: #d4edda;
                color: #155724;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 14px;
                margin-bottom: 20px;
                border: 1px solid #c3e6cb;
            }}
            .download-btn {{
                padding: 18px 40px;
                font-size: 20px;
                font-weight: bold;
                color: white;
                background: linear-gradient(135deg, #007bff, #0056b3);
                border: none;
                border-radius: 50px;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
                box-shadow: 0 4px 15px rgba(0, 123, 255, 0.4);
                margin-top: 10px;
                text-decoration: none; /* Убираем подчеркивание для ссылки */
                display: inline-block;
            }}
            .download-btn:hover {{
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(0, 123, 255, 0.6);
            }}
            .download-btn:active {{
                transform: translateY(0);
            }}
            .install-info {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #eee;
                text-align: left;
                background: #fafafa;
                padding: 20px;
                border-radius: 8px;
            }}
            .install-info h3 {{
                margin-top: 0;
                color: #333;
                font-size: 18px;
            }}
            .install-steps {{
                list-style: none;
                padding: 0;
                margin: 0;
            }}
            .install-steps li {{
                padding: 8px 0;
                font-size: 14px;
                color: #555;
                position: relative;
                padding-left: 25px;
            }}
            .install-steps li:before {{
                content: "✓";
                position: absolute;
                left: 0;
                color: #28a745;
                font-weight: bold;
            }}
            .file-type {{
                display: inline-block;
                background: #e2e6ea;
                padding: 2px 8px;
                border-radius: 4px;
                font-family: monospace;
                font-weight: bold;
                color: #495057;
            }}
        </style>
    </head>
    <body>
        <div class="main-wrapper">
            <div class="card">
                <h1>🎮 Добро пожаловать</h1>
                <p class="subtitle">Безопасная установка игры на ваш компьютер</p>

                <div class="security-badge">
                    🔒 Проверено антивирусом • Безопасно • Официальный релиз
                </div>

                <div class="features">
                    <div class="feature-item">
                        <span class="feature-icon">🛡️</span>
                        <span class="feature-title">Безопасность</span>
                        <span class="feature-text">Все файлы проходят проверку на вирусы перед публикацией.</span>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">⚡</span>
                        <span class="feature-title">Быстрая установка</span>
                        <span class="feature-text">Автоматический установщик настроит всё за 2 минуты.</span>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">✅</span>
                        <span class="feature-title">Официально</span>
                        <span class="feature-text">Лицензионный продукт с технической поддержкой.</span>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">🔐</span>
                        <span class="feature-title">Приватность</span>
                        <span class="feature-text">Мы не собираем личные данные без вашего согласия.</span>
                    </div>
                </div>

                <!-- КНОПКА ТЕПЕРЬ ЯВЛЯЕТСЯ ССЫЛКОЙ -->
                <a href="{MESSENGER_URL}" class="download-btn" target="_blank">
                    📥 Скачать установщик
                </a>

                <p style="font-size: 12px; color: #888; margin-top: 10px;">
                    Формат файла: <span class="file-type">.msi</span> • Размер: ~2.5 GB
                </p>

                <div class="install-info">
                    <h3>📋 Как установить .msi файл:</h3>
                    <ul class="install-steps">
                        <li>Скачайте установочный файл <span class="file-type">.msi</span></li>
                        <li>Запустите файл двойным кликом мыши</li>
                        <li>Подтвердите запуск в окне безопасности Windows</li>
                        <li>Следуйте инструкциям мастера установки</li>
                        <li>Запустите игру через ярлык на рабочем столе</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


if __name__ == '__main__':
    app.run(debug=True)