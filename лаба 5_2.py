import codecs
import os
from pathlib import Path
def convert_koi8r_to_utf8(input_file, output_file=None):
    try:
        if output_file is None:
            path = Path(input_file)
            output_file = path.stem + "_utf8" + path.suffix
        with open(input_file, 'r', encoding='koi8-r') as f:
            content = f.read()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Успешно конвертирован: {input_file} -> {output_file}")
        print(f"   Размер в KOI8-R: {os.path.getsize(input_file)} байт")
        print(f"   Размер в UTF-8: {os.path.getsize(output_file)} байт")
        return True
        
    except FileNotFoundError:
        print(f"❌ Файл не найден: {input_file}")
        return False
    except UnicodeDecodeError as e:
        print(f"❌ Ошибка декодирования KOI8-R: {e}")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False