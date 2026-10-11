# ============================================================
#  Расчёт оборотов — мобильная версия на Kivy
#  Формула: n = (1000 * V) / (π * D)
#  Интерфейс ПРИЖАТ К ВЕРХУ экрана (маленький отступ сверху)
# ============================================================

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp

# Цвет фона окна (тёмно-серый)
Window.clearcolor = (0.15, 0.15, 0.18, 1)


class OborotiApp(App):
    """Главный класс приложения."""

    def build(self):
        # Вертикальный контейнер.
        # padding=[left, top, right, bottom]:
        #   сверху dp(10) — маленький отступ
        #   снизу dp(0)  — не тратим место
        layout = BoxLayout(
            orientation='vertical',
            padding=[dp(30), dp(10), dp(30), 0],
            spacing=dp(10)
        )

        # ---------- Заголовок ----------
        layout.add_widget(Label(
            text="Расчёт оборотов",
            font_size='22sp',
            size_hint=(1, None),
            height=dp(40),
            color=(1, 1, 1, 1)
        ))

        # ---------- Подпись: Диаметр ----------
        layout.add_widget(Label(
            text="Диаметр (мм):", font_size='17sp',
            size_hint=(1, None), height=dp(28),
            color=(0.9, 0.9, 0.9, 1)
        ))

        # ---------- Поле: Диаметр ----------
        self.dia_input = TextInput(
            multiline=False,
            input_filter='float',
            font_size='20sp',
            size_hint=(1, None),
            height='48dp',
            halign='center',
            padding=[dp(10), dp(10), dp(10), dp(10)],
            background_color=(0.25, 0.25, 0.3, 1),
            foreground_color=(1, 1, 1, 1)
        )
        layout.add_widget(self.dia_input)

        # ---------- Подпись: Скорость ----------
        layout.add_widget(Label(
            text="Скорость (м/мин):", font_size='17sp',
            size_hint=(1, None), height=dp(28),
            color=(0.9, 0.9, 0.9, 1)
        ))

        # ---------- Поле: Скорость ----------
        self.skr_input = TextInput(
            multiline=False,
            input_filter='float',
            font_size='20sp',
            size_hint=(1, None),
            height='48dp',
            halign='center',
            padding=[dp(10), dp(10), dp(10), dp(10)],
            background_color=(0.25, 0.25, 0.3, 1),
            foreground_color=(1, 1, 1, 1)
        )
        layout.add_widget(self.skr_input)

        # ---------- Кнопка "Рассчитать" ----------
        btn = Button(
            text="Рассчитать", font_size='20sp',
            size_hint=(1, None),
            height='54dp',
            background_color=(0.3, 0.7, 0.3, 1)
        )
        btn.bind(on_press=self.calculate)
        layout.add_widget(btn)

        # ---------- Метка результата ----------
        self.result_label = Label(
            text="Обороты = —", font_size='22sp',
            size_hint=(1, None), height=dp(50),
            color=(1, 1, 1, 1)
        )
        layout.add_widget(self.result_label)

        # ---------- «Распорка» снизу ----------
        # Пустой виджет с size_hint=(1, 1) — он заберёт ВСЁ
        # свободное место внизу и прижмёт остальное к верху.
        layout.add_widget(Widget(size_hint=(1, 1)))

        return layout

    # ============================================================
    #  Расчёт: читаем поля, считаем по формуле, показываем ответ
    # ============================================================
    def calculate(self, instance):
        try:
            dia = float(self.dia_input.text.replace(",", "."))
            skr = float(self.skr_input.text.replace(",", "."))

            if dia == 0:
                self.result_label.text = "Диаметр не может быть 0"
                self.result_label.color = (1, 0.3, 0.3, 1)
                return

            n = (1000 * skr) / (dia * 3.14)

            self.result_label.text = f"Обороты = {n:.2f}"
            self.result_label.color = (0.5, 1, 0.5, 1)

        except ValueError:
            self.result_label.text = "Введи числа!"
            self.result_label.color = (1, 0.3, 0.3, 1)


# ============================================================
#  Точка входа
# ============================================================
if __name__ == "__main__":
    OborotiApp().run()