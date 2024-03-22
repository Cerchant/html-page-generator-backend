# Используем официальный образ Python в качестве базового образа
FROM python
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
# Копируем файл requirements.txt внутрь контейнера
COPY . .
# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r Django

CMD ["python", "manage.py"]