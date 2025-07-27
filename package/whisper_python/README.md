# Whisper Python

**Whisper Python** {description}

- 🇮🇩 [Indonesia](https://github.com/zerounintezaragler/whisper_python/blob/main/README.md)
- 🇨🇿 [Afrika](https://github.com/zerounintezaragler/whisper_python/blob/main/README_AFRIKA.md)
- 🇨🇳 [China](https://github.com/zerounintezaragler/whisper_python/blob/main/README_CHINA.md)
- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 [English](https://github.com/zerounintezaragler/whisper_python/blob/main/README_ENGLISH.md)
- 🇮🇳 [India](https://github.com/zerounintezaragler/whisper_python/blob/main/README_INDIA.md)
- 🇮🇩 [Jawa](https://github.com/zerounintezaragler/whisper_python/blob/main/README_JAWA.md)
- 🇯🇵 [Jepang](https://github.com/zerounintezaragler/whisper_python/blob/main/README_JEPANG.md)
- 🇰🇷 [Korea](https://github.com/zerounintezaragler/whisper_python/blob/main/README_KOREA.md)
- 🇷🇺 [Russia](https://github.com/zerounintezaragler/whisper_python/blob/main/README_RUSSIA.md)
- 🇮🇩 [Sunda](https://github.com/zerounintezaragler/whisper_python/blob/main/README_SUNDA.md)
- 🇹🇭 [Thailand](https://github.com/zerounintezaragler/whisper_python/blob/main/README_THAILAND.md)

## Fakta

- Library ini tidak terikat banyak depenencides pihak 3

## Feature

- [x] **Sangat Cepat** Library Async (**Tidak Memblokir Threads**)
- [x] **Mudah Digunakan**

## Contoh

- [Contoh Sederhana](https://github.com/zerounintezaragler/whisper_python/tree/main/quickstart)

## Memasang

sebelum memasang pastikan kamu mengetahui basic python setidaknya kamu sudah menginstall ptyhon dalam komputer / device kamu. [Python Website](https://www.python.org)

- **Python**

  ```bash
  pip install whisper-python
  ```

## Dokumentasi

### EnsureInitialized

method wajib di panggil bebas mau setelah **on** / sebelum method **on** tapi saya sarankan sebelum **on**

**contoh:**

```python
  whisperPythonZerounIntezarAgler.ensureInitialized(libraryPath="fork/dependencies/lib/libwhisper_python.so")
```

### Initialized

method ini wajib di panggil setelah method **on** karena untuk mengolah update

**contoh:**

```python
  await whisperPythonZerounIntezarAgler.initialized()
```

### On

method on ini berguna untuk mendapatkan update data dari invoke / update

**contoh:**

```python

  def on_callback(update:dict):
    print(update)

  whisperPythonZerounIntezarAgler.on(event_name="update", on_callback=on_callback)
  
```


### loadModelFromFilePath

pastikan kamu meload model dahulu ya agar bisa transcribe

**contoh:**

```python
    result =await whisperPythonZerounIntezarAgler.loadModelFromFilePath(whisperModelFilePath="../../../big-data/whisper/ggml-base.en.bin")
    print(result)
```


### transcribeFromFilePath

transcribe untuk mendapatkan teks

**contoh:**

```python
    translate=await whisperPythonZerounIntezarAgler.transcribeFromFilePath(file_path="../../../fork/whisper.cpp/samples/jfk.mp3")
    print(translate)
```

## Bantuan

**Sulit**? saya sudah membangun **library** ini **sebaik** mungkin dan **berusaha mudah** di baca dan **digunakan sebaik mungkin**. 

jika **kamu** masih **merasa** **kesulitan** dan **kebingungan** **cobalah bergabung** ke **group** kami secara **gratis tanpa biaya apapun**

- [Telegram](https://t.me/DEVELOPER_GLOBAL_PUBLIC)

**sebelum join** pastikan **memakai profile** yang **jelas** kami tidak keberatan kamu siapa, dan pangkat apapun, tapi **pastikan** **ada username dan photo profile**, dan usahakan untuk **chat di group** **tidak chat pribadi** karena itu **group umum dan mungkin orang lain kebingungan**. jika **tidak mengikuti** ini kemungkinan **tidak bisa akses chat di group dan bakal di banned**, solusi pakai akun kedua, karena setelah di banned kami tidak bisa merespond cepat


## Support Me

Jika kamu merasa program ini berguna, kamu bisa support saya [GITHUB Zeroun Intezar Agler](https://github.com/zerounintezaragler) di link itu tersedia social media dan sponsor saya. saya tidak keberatan jika kamu hanya follow / donasi uang sedikit

![]({gopay_qr_url})

- https://github.com/sponsors/zerounintezaragler
- https://www.patreon.com/c/{patreon_username}
- https://opencollective.com/{opencollective_username}
- https://paypal.me/{paypal_username}

Terimakasih


zerounintezaragler - 27-07-2025


## Tags

- whisper_python python

