import qrcode
# пример данных
data = "https://one.okkam.group/"
# имя конечного файла
filename = "okkam.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)
