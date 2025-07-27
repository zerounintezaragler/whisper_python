# Whisper Python

** Whisper Python ** Получите текст из любого аудио, без оплаты, бесплатно, не нуждаясь в GPU и не нужно конвертировать FFMPEG

- 🇮🇩 [Индонезия] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme.md)
- 🇺🇸 [английский] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_en.md)
- 🇰🇷 [Корея, Республика Южная Корея] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ko.md)
- 🇨🇳 [Китай] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_zh-cn.md)
- 🇿🇦 [Южная Африка] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_af.md)
- 🇮🇳 [Индия] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_hi.md)
- 🇯🇵 [Япония] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ja.md)
- 🇷🇺 [Россия] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ru.md)
- 🇹🇭 [Таиланд] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_th.md)
- 🇦🇪 [United Arab Emirates] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ar.md)

## факт

- Эта библиотека не связана многими зависимостями 3
- Нет необходимости в ffmpeg

## Особенность

- [x] ** очень быстро ** библиотека Ashnc
- [x] ** проще в использовании **

## Пример

- [простой пример] (https://github.com/zerounintezaragler/whisper_python/tree/main/quickstart)

## Установить

Перед установкой убедитесь, что вы знаете Basic Python, по крайней мере, вы установили Ptyhon на свой компьютер / устройство. [Веб -сайт Python] (https://www.python.org)

- ** python **

  `` `Bash
  PIP Установите Whisper-Python
  `` `

## документация

### убедитесь, что

Метод должен называться свободно хочу быть после ** на ** / до метода ** на **, но я предлагаю до ** на **

**пример:**

`` Python
  Whisperpythonzerountintezaragler.ensureInitialize (LibraryPath = "fork/зависимости/lib/libwhisper_python.so")
`` `

### Инициализирован

Этот метод должен быть вызван после ** на ** метод, потому что для обработки обновлений

**пример:**

`` Python
  Ждать whisperpythonzerountezaragler.initialized ()
`` `

### На

Этот метод полезен для получения обновлений данных из вызовов / обновлений

**пример:**

`` Python

  def on_callback (обновление: dict):
    Печать (обновление)

  Whisperpythonzerountezaragler.on (event_name = "update", on_callback = on_callback)
  
`` `


### LoadModelfromFilePath

Убедитесь, что вы сначала загрузили модель, чтобы вы могли транскрибировать

**пример:**

`` Python
    РЕЗУЛЬТАТ = watiat whisperpythonzerountezaragler.loadmodelfromfilepath (Whispermodelfilekat = "../../../ Big-Data/Whisper/Ggml-base.en.bin")
    Печать (результат)
`` `


### Транскрибибельсфромфилекат

Транскрибция, чтобы получить текст

**пример:**

`` Python
    Translate = await whisperpythonzerountezaragler.transcribefromfilekat (file_path = "../../../../../ fork/whisper.cpp/samples/jfk.mp3")
    Печать (перевод)
`` `

## Помощь

**Трудный**? Я построил ** библиотеку ** это ** как можно больше **, может быть, и ** попробуйте легко **, чтобы прочитать и ** использованный как можно лучше **. 

Если ** ты ** все еще ** почувствуешь ** ** Сложность ** и ** Стушение ** ** Попробуй присоединиться ** к ** Группе ** Мы в ** бесплатно без каких -либо затрат **

- [Telegram] (https://t.me/developer_global_public)

** Прежде чем присоединиться **, убедитесь, что ** используйте профиль **, что ** ясно ** Мы не возражаем против того, кто вы, и любое звание, но ** убедитесь, что ** ** Есть имя пользователя и фотопрофиль **, и постарайтесь ** поболтать в группе ** ** Нет личного чата **, потому что это ** Общая группа и, возможно, другие люди не смущены **. Если ** не следует ** это возможность ** не может получить доступ к чату в группе и будет запрещено **, решение использовать вторую учетную запись, потому что после того, как мы запрещены, мы не можем быстро ответить


## поддержите меня

Если вы чувствуете, что эта программа полезна, вы можете поддержать меня [Github Zeroun Intezar Agler] (https://github.com/zerounintezaragler) на ссылке доступны в социальных сетях, а мои спонсоры. Я не против, если вы только следовали / пожертвовали немного денег

Спасибо

Zerounintezaragler-27-07-2025## теги

- Whisper_python Python