import os


# Функция для создания структуры каталогов
def create_directory_structure(base_path, structure):
    for folder_name, content in structure.items():
        folder_path = os.path.join(base_path, folder_name)

        # Если это не README.md, создаем папку
        if folder_name != "README.md":
            os.makedirs(folder_path, exist_ok=True)

        # Если это README.md, создаем файл
        if folder_name == "README.md":
            readme_path = os.path.join(base_path, folder_name)
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
        # Если это словарь, рекурсивно обрабатываем вложенные элементы
        elif isinstance(content, dict):
            create_directory_structure(folder_path, content)


# Структура проекта
project_structure = {
    "Articles": {
        "README.md": """
# Articles
В этом разделе находятся статьи, разделенные на следующие категории:
- **Scientific**: Научные статьи и исследования.
- **Review**: Обзорные статьи по различным темам.
- **Technical**: Технические статьи и руководства.
""",
        "Scientific": {},
        "Review": {},
        "Technical": {},
    },
    "Projects": {
        "README.md": """
# Projects
В этом разделе хранятся проекты, включая Python проекты, и задачи, которые нужно завершить.
""",
        "Python Projects": {},
        "To Do": {},
    },
    "Development": {
        "README.md": """
# Development
Заметки по разработке программного обеспечения, включая языки программирования, фреймворки и инструменты.
""",
        "Python": {
            "Frameworks": {},
            "Libraries": {},
        },
        "Git": {},
        "CSS": {},
        "Github": {},
        "Google Colab": {},
        "HTML": {},
        "JavaScript": {},
        "JQuery": {},
        "Markdown": {},
        "Powershell": {},
        "SQL": {},
    },
    "Media": {
        "README.md": """
# Media
Раздел заметок по медиа-контенту.
""",
        "Anime": {},
        "Movies": {},
        "Series": {},
    },
    "Sites": {},
    "Contacts": {},
    "Diary": {},
    "Games": {},
    "Ideas": {},
    "Obsidian": {
        "README.md": """
# Obsidian
Заметки о настройке и использовании Obsidian.
""",
        "Plugins": {},
        "Theme": {},
    },
    "AI": {},
    "Books": {},
    "Education": {},
    "Soft": {},
}

# Основной путь, куда будет создана структура (текущая директория)
base_path = os.getcwd()

# Создание структуры каталогов
create_directory_structure(base_path, project_structure)

print(f"Структура проекта успешно создана в {base_path}")
