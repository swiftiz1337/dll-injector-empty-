# DLL Injector GUI

Простой графический интерфейс для выбора процесса и DLL-файла. Проект создан с использованием PyQt5 и предназначен для образовательных целей.

![Screenshot](screenshot.png) <!-- Добавьте скриншот интерфейса -->

## Особенности
- Выбор процесса из списка запущенных процессов.
- Выбор DLL-файла через диалоговое окно.
- Уведомления об ошибках и успешных операциях.
- Стильный и минималистичный дизайн.

## Установка

1. Убедитесь, что у вас установлен Python 3.7 или выше.
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/dll-injector-gui.git
   cd dll-injector-gui
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

1. Запустите программу:
   ```bash
   python main.py
   ```
2. Выберите процесс из выпадающего списка.
3. Нажмите "Выбрать DLL" и выберите DLL-файл.
4. Нажмите "Inject" для выполнения операции.

## Логика инжекта

Логика инжекта DLL была удалена из проекта. Если вы хотите добавить её самостоятельно, следуйте инструкциям ниже.

### Как добавить логику инжекта

1. Используйте библиотеку `pymem` или Windows API для работы с процессами.
2. Реализуйте следующие шаги:
   - Откройте процесс с помощью `OpenProcess`.
   - Выделите память в целевом процессе с помощью `VirtualAllocEx`.
   - Запишите путь к DLL в выделенную память с помощью `WriteProcessMemory`.
   - Создайте удалённый поток для вызова `LoadLibrary` с помощью `CreateRemoteThread`.
3. Добавьте свою реализацию в метод `inject` в файле `main.py`.

Пример реализации можно найти в [этом руководстве](https://github.com/srounet/Pymem).

## Зависимости

- `PyQt5` — для создания графического интерфейса.
- `psutil` — для получения списка процессов.
- `pymem` — для работы с процессами (необязательно, если вы добавляете свою логику).

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

### Дополнительные файлы

1. **`requirements.txt`**:
   ```plaintext
   PyQt5==5.15.9
   psutil==5.9.0
   pymem==1.10.0
   ```

2. **`.gitignore`**:
   ```plaintext
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   .env
   venv/
   ```

3. **`LICENSE`** (пример MIT лицензии):
   ```plaintext
   MIT License

   Copyright (c) 2023 Ваше Имя

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.
   ```

---

### Как залить на GitHub

1. Создайте новый репозиторий на GitHub.
2. Инициализируйте Git в вашем проекте:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Свяжите локальный репозиторий с удалённым:
   ```bash
   git remote add origin https://github.com/ваш-username/dll-injector-gui.git
   ```
4. Загрузите изменения:
   ```bash
   git push -u origin master
   ```

Теперь ваш проект будет доступен на GitHub!
