# Fluister python

** Whisper Python ** Kry teks van enige klank sonder om te betaal, gratis vanlyn, geen nodige GPU nie, en hoef nie FFMPEG te omskep nie

- 🇮🇩 [Indonesië] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme.md)
- 🇨🇿 [Afrika] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_afrika.md)
- 🇨🇳 [China] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_china.md)
- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 [Engels] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_english.md)
- 🇮🇳 [Indië] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_india.md)
- 🇮🇩 [Java] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_jawa.md)
- 🇯🇵 [Japannees] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_jepang.md)
- 🇰🇷 [Korea] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_korea.md)
- 🇷🇺 [Rusland] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_russia.md)
- 🇮🇩 [Sundanese] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_sunda.md)
- 🇹🇭 [Thailand] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_thailand.md)

## feit

- Hierdie biblioteek is nie gebind deur baie afhanklikhede nie 3
- Geen behoefte aan ffmpeg nie

## funksie

- [x] ** baie vinnig ** ashnc -biblioteek
- [x] ** maklik om te gebruik **

## Voorbeeld

- [Eenvoudige voorbeeld] (https://github.com/zerounintezaragler/whisper_python/tree/main/quickstart)

## Installeer

Voordat u installeer, moet u seker maak dat u die basiese python ten minste ken, u Ptyhon op u rekenaar / toestel geïnstalleer het. [Python webwerf] (https://www.python.org)

- ** Python **

  `` Bash
  Pip installeer fluister python
  `` `

## dokumentasie

### Versekeryninaliseer

Die metode moet vrylik genoem word om na ** op ** / voor die metode ** op ** te wees, maar ek stel voor ** op **

** Voorbeeld: **

`` `Python
  Whisperpythonzerounintezaragler.ensureInitialized (LibraryPath = "Fork/Dependencies/lib/libwhisper_python.so")
`` `

### Initialiseer

Hierdie metode moet na die ** op ** -metode geroep word, want om opdaterings te verwerk

** Voorbeeld: **

`` `Python
  Wag op fluisterpythonzerounintezaragler.initialized ()
`` `

### aan

Hierdie metode is nuttig om data -opdaterings van oproepe / opdaterings te kry

** Voorbeeld: **

`` `Python

  def on_callback (opdatering: dict):
    Druk (opdatering)

  WhisperPythonzerounintezaragler.on (event_name = "update", on_callback = on_callback)
  
`` `


### loadmodelfromfilepath

Maak seker dat u die model eers laai sodat u kan transkribeer

** Voorbeeld: **

`` `Python
    resultaat = wag op fluisterpythonzerounintezaragler.loadmodelfromfilepath (fluistermodelfilekat = "../../../ big-data/fluister/ggml-base.en.bin")
    Druk (resultaat)
`` `


### Transkribefromfilekath

transkribeer om teks te kry

** Voorbeeld: **

`` `Python
    translate = wag op fluisterpythonzerounintezaragler.transcribefromfilekat (file_path = "../../../../ vurk/fluister.cpp/monsters/jfk.mp3")
    Druk (vertaal)
`` `

## Help

** Moeilik **? Ek het ** biblioteek ** hierdie ** so goed as moontlik ** gebou en ** probeer maklik ** om te lees en ** so goed as moontlik gebruik **. 

As ** jy ** nog steeds ** voel ** ** Moeilikheid ** en ** Verwarring ** ** Probeer om aan te sluit ** tot ** Groep ** Ons in ** gratis sonder enige koste **

- [Telegram] (https://t.me/developer_global_public)

** Voordat u aansluit ** maak seker ** Gebruik profiel ** dat ** duidelik ** Ons gee nie om wie u is nie, en enige rang, maar ** Maak seker dat daar 'n gebruikersnaam en fotoprofiel is **, en probeer om ** in die groep te gesels ** ** Geen persoonlike klets ** want dit ** General Group en miskien is ander mense verward **. As ** nie volg nie **, is dit die moontlikheid ** kan nie toegang hê tot die klets in die groep nie en sal dit verbied word **, die oplossing om die tweede rekening te gebruik, want nadat ons verbied is, kan ons nie vinnig reageer nie


## Ondersteun my

As u voel dat hierdie program nuttig is, kan u my ondersteun [GitHub Zeroun Intezar Agler] (https://github.com/zerounintezaragler) op die skakel is beskikbaar op sosiale media en my borge. Ek gee nie om nieAs u net 'n bietjie geld volg / skenk

Dankie

Zerounintezaragler-27-07-2025


## Tags

- fluister_python python