from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'super_secret_key_change_this'  # Нужен для работы сессий

# Список вопросов (можно легко редактировать)
QUESTIONS = [
    {
        'id': 1,
        'question': 'Как вас зовут?',
        'type': 'text',
        'placeholder': 'Введите ваше имя'
    },
    {
        'id': 2,
        'question': 'Сколько вам лет?',
        'type': 'number',
        'placeholder': 'Введите возраст'
    },
    {
        'id': 3,
        'question': 'Какой ваш любимый цвет?',
        'type': 'choice',
        'options': ['Красный', 'Синий', 'Зелёный', 'Жёлтый', 'Другой']
    },
    {
        'id': 4,
        'question': 'Нравится ли вам программировать?',
        'type': 'choice',
        'options': ['Да, очень!', 'Иногда', 'Нет, не особо']
    },
    {
        'id': 5,
        'question': 'Оставьте комментарий (необязательно)',
        'type': 'text',
        'placeholder': 'Ваши пожелания...',
        'required': False
    }
]

# HTML-шаблон главной страницы (вопросы)
QUESTION_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Опрос | Вопрос {{ current_question + 1 }} из {{ total_questions }}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
            width: 100%;
        }
        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e0e0e0;
            border-radius: 4px;
            margin-bottom: 30px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 4px;
            transition: width 0.3s ease;
        }
        .question-number {
            color: #667eea;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .question-text {
            font-size: 24px;
            color: #333;
            margin-bottom: 30px;
            line-height: 1.4;
        }
        .form-group {
            margin-bottom: 25px;
        }
        .form-control {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        .form-control:focus {
            outline: none;
            border-color: #667eea;
        }
        .choice-group {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .choice-option {
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
        }
        .choice-option:hover {
            border-color: #667eea;
            background: #f8f9ff;
        }
        .choice-option input {
            margin-right: 15px;
            width: 20px;
            height: 20px;
        }
        .choice-option.selected {
            border-color: #667eea;
            background: #f0f3ff;
        }
        .btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 10px;
            display: none;
        }
        .error.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="progress-bar">
            <div class="progress-fill" style="width: {{ ((current_question + 1) / total_questions) * 100 }}%"></div>
        </div>

        <div class="question-number">Вопрос {{ current_question + 1 }} из {{ total_questions }}</div>
        <h1 class="question-text">{{ question.question }}</h1>

        <form id="questionForm" method="POST" action="/submit_answer">
            {% if question.type == 'text' or question.type == 'number' %}
                <div class="form-group">
                    <input 
                        type="{{ question.type }}" 
                        name="answer" 
                        class="form-control" 
                        placeholder="{{ question.placeholder }}"
                        {% if question.get('required', True) %}required{% endif %}
                    >
                </div>
            {% elif question.type == 'choice' %}
                <div class="form-group choice-group">
                    {% for option in question.options %}
                        <label class="choice-option">
                            <input type="radio" name="answer" value="{{ option }}" required>
                            {{ option }}
                        </label>
                    {% endfor %}
                </div>
            {% endif %}

            <div class="error" id="errorMsg">Пожалуйста, ответьте на вопрос</div>
            <button type="submit" class="btn">
                {% if current_question + 1 < total_questions %}
                    Далее →
                {% else %}
                    Завершить ✓
                {% endif %}
            </button>
        </form>
    </div>

    <script>
        // Подсветка выбранных вариантов
        document.querySelectorAll('.choice-option').forEach(option => {
            option.addEventListener('click', function() {
                document.querySelectorAll('.choice-option').forEach(o => o.classList.remove('selected'));
                this.classList.add('selected');
            });
        });

        // Валидация формы
        document.getElementById('questionForm').addEventListener('submit', function(e) {
            const answer = document.querySelector('[name="answer"]:checked') || 
                          document.querySelector('[name="answer"]').value;
            if (!answer) {
                e.preventDefault();
                document.getElementById('errorMsg').classList.add('show');
            }
        });
    </script>
</body>
</html>
"""

# HTML-шаблон страницы результатов
RESULT_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Результаты опроса</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
        }
        .success-icon {
            font-size: 60px;
            text-align: center;
            margin-bottom: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        .answers-list {
            list-style: none;
            margin-bottom: 30px;
        }
        .answer-item {
            padding: 15px;
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
        }
        .answer-item:last-child {
            border-bottom: none;
        }
        .answer-question {
            color: #666;
            font-size: 14px;
            flex: 1;
        }
        .answer-value {
            color: #667eea;
            font-weight: 600;
            text-align: right;
            flex: 1;
        }
        .btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
            text-decoration: none;
            display: block;
            text-align: center;
        }
        .btn:hover {
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="success-icon">🎉</div>
        <h1>Спасибо за ответы!</h1>

        <ul class="answers-list">
            {% for item in answers %}
            <li class="answer-item">
                <span class="answer-question">{{ item.question }}</span>
                <span class="answer-value">{{ item.answer }}</span>
            </li>
            {% endfor %}
        </ul>

        <a href="/restart" class="btn">Пройти заново ↻</a>
    </div>
</body>
</html>
"""


@app.route('/')
def index():
    # Инициализация сессии при первом заходе
    if 'current_question' not in session:
        session['current_question'] = 0
        session['answers'] = []

    current_q = session['current_question']

    # Если все вопросы пройдены - redirect на результаты
    if current_q >= len(QUESTIONS):
        return redirect(url_for('results'))

    return render_template_string(
        QUESTION_TEMPLATE,
        question=QUESTIONS[current_q],
        current_question=current_q,
        total_questions=len(QUESTIONS)
    )


@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form.get('answer', '').strip()

    if not answer:
        return redirect(url_for('index'))  # Если пусто - остаёмся на том же вопросе

    # Сохраняем ответ
    if 'answers' not in session:
        session['answers'] = []

    session['answers'].append({
        'question': QUESTIONS[session['current_question']]['question'],
        'answer': answer
    })

    # Переход к следующему вопросу
    session['current_question'] += 1
    session.modified = True

    return redirect(url_for('index'))


@app.route('/results')
def results():
    if 'answers' not in session or not session['answers']:
        return redirect(url_for('index'))

    return render_template_string(
        RESULT_TEMPLATE,
        answers=session['answers']
    )


@app.route('/restart')
def restart():
    # Сброс сессии
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)