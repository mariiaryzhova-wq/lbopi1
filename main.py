import datetime

class AnswerBetterProcessor:
    def __init__(self):
        self.version = "0.1"
        self.tones = ["Professional", "Confident", "Friendly"]

    def transform_text(self, text, tone):
        """
        Основна логіка трансформації тексту (симуляція для ЛР)
        """
        if not text:
            return "Помилка: Текст порожній"

        # Логіка вибору відповіді залежно від тону
        responses = {
            "Professional": "Дякую за повідомлення. Я опрацюю цей запит і надам відповідь найближчим часом.",
            "Confident": "Я отримав ваш запит. Повернуся з відповіддю, як тільки звільниться час у моєму графіку.",
            "Friendly": "Привіт! Дякую, що написали. Скоро повернуся до вас із деталями!"
        }
        
        return responses.get(tone, "Тон не знайдено")

    # КРОК 6: AI-ЗГЕНЕРОВАНА ФУНКЦІЯ
    # Промпт: "Напиши метод класу на Python, який генерує психологічне 
    # обґрунтування змін у тексті для проєкту AnswerBetter"
    def get_psychological_explanation(self, tone):
        explanations = {
            "Professional": "Ми використали нейтральну лексику, щоб змістити фокус з особистостей на робочі процеси.",
            "Confident": "Ми прибрали вибачальні конструкції ('вибачте', 'мабуть'), щоб ви звучали більш рішуче.",
            "Friendly": "Ми додали слова ввічливості та окличні знаки для створення позитивного емоційного фону."
        }
        return explanations.get(tone, "Пояснення готується...")

def main():
    processor = AnswerBetterProcessor()
    
    print(f"--- AnswerBetter CLI (v{processor.version}) ---")
    user_input = input("Введіть текст для обробки: ")
    print("\nОберіть тон: 1. Professional, 2. Confident, 3. Friendly")
    choice = input("Ваш вибір (номер): ")
    
    tone_map = {"1": "Professional", "2": "Confident", "3": "Friendly"}
    selected_tone = tone_map.get(choice, "Professional")

    result = processor.transform_text(user_input, selected_tone)
    why = processor.get_psychological_explanation(selected_tone)

    print("\n" + "="*30)
    print(f"ТРАНСФОРМОВАНИЙ ТЕКСТ:\n{result}")
    print(f"\nЧОМУ ЦЕ ПРАЦЮЄ (The Why Factor):\n{why}")
    print("="*30)
    print(f"Дата обробки: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

if __name__ == "__main__":
    main()
