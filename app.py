import mimetypes
import gradio as gr

# Функция для определения MIME-типа файла
def identify_file_type(file):
    mime_type, _ = mimetypes.guess_type(file.name)
    return mime_type if mime_type else 'Не удалось определить тип'

# Функция для создания вопросов на основе текста
def generate_questions(text):
    sentences = text.split('. ')
    questions = []

    for i in range(min(5, len(sentences))):
        question = f"Что вы можете сказать о следующем: '{sentences[i]}?'"
        questions.append(question)

    return questions

# Функция для обработки загруженного файла
def process_file(file):
    content = file.read().decode('utf-8')
    questions = generate_questions(content)
    return questions

# Функция для оценки ответов
def evaluate_answers(*answers):
    correct_answers = len(answers)  # Подсчет всех ответов
    return f"Вы ответили на {correct_answers} вопрос(ов)."

# Создаем Gradio интерфейс
def launch_gradio_interface():
    interface = gr.Interface(
        fn=process_file,
        inputs=gr.File(label="Загрузите текстовый файл"),
        outputs="text",
        title="Ответьте на вопросы",
        description="Загрузите текстовый файл и получите вопросы."
    )
    interface.launch()

# Запускаем интерфейс
if __name__ == "__main__":
    launch_gradio_interface()
