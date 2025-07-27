# Whisper Python

** Whisper Python ** รับข้อความจากเสียงใด ๆ โดยไม่ต้องจ่ายเงินฟรีออฟไลน์ไม่จำเป็นต้องใช้ GPU และไม่จำเป็นต้องแปลง FFMPEG

- 🇮🇩 [อินโดนีเซีย] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme.md)
- 🇺🇸 [ภาษาอังกฤษ] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_en.md)
- 🇰🇷 [เกาหลีสาธารณรัฐเกาหลีใต้] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ko.md)
- 🇨🇳 [จีน] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_zh-cn.md)
- 🇿🇦 [แอฟริกาใต้] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_af.md)
- 🇮🇳 [อินเดีย] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_hi.md)
- 🇯🇵 [ญี่ปุ่น] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ja.md)
- 🇷🇺 [รัสเซีย] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ru.md)
- 🇹🇭 [ไทย] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_th.md)
- 🇦🇪 [สหรัฐอาหรับเอมิเรตส์] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ar.md)

## ข้อเท็จจริง

- ห้องสมุดนี้ไม่ผูกพันกับการพึ่งพาจำนวนมาก 3
- ไม่จำเป็นต้องใช้ ffmpeg

## คุณสมบัติ

- [x] ** เร็วมาก ** ASHNC Library
- [x] ** ใช้งานง่าย **

## ตัวอย่าง

- [ตัวอย่างง่ายๆ] (https://github.com/zerounintezaragler/whisper_python/tree/main/quickstart)

## ติดตั้ง

ก่อนที่จะติดตั้งตรวจสอบให้แน่ใจว่าคุณรู้ว่า Python พื้นฐานอย่างน้อยคุณก็ติดตั้ง ptyhon บนคอมพิวเตอร์ / อุปกรณ์ของคุณ [เว็บไซต์ Python] (https://www.python.org)

- ** Python **

  `` `ทุบตี
  PIP ติดตั้ง Whisper-Python
  -

## เอกสาร

### ตรวจสอบให้แน่ใจ

วิธีการนี้จะต้องเรียกอย่างอิสระต้องการหลังจาก ** บน ** / ก่อนวิธีการ ** บน ** แต่ฉันแนะนำก่อน ** บน **

**ตัวอย่าง:**

`` `Python
  Whisperpythonzerounintezaragler.ensureInitialized (LibraryPath = "ส้อม/การพึ่งพา/lib/libwhisper_python.so"))
-

### เริ่มต้น

วิธีนี้จะต้องเรียกหลังจากวิธี ** บน ** เพราะจะประมวลผลการอัปเดต

**ตัวอย่าง:**

`` `Python
  รอ whisperpythonzerounintezaragler.initialized ()
-

### บน

วิธีนี้มีประโยชน์สำหรับการอัปเดตข้อมูลจากการเรียกใช้ / การอัปเดต

**ตัวอย่าง:**

`` `Python

  def on_callback (อัปเดต: dict):
    พิมพ์ (อัปเดต)

  whisperpythonzerounintezaragler.on (event_name = "update", on_callback = on_callback)
  
-


### loadmodelfromfilepath

ตรวจสอบให้แน่ใจว่าคุณโหลดโมเดลก่อนเพื่อให้คุณสามารถถอดความได้

**ตัวอย่าง:**

`` `Python
    ผลลัพธ์ = รอ whisperpythonzerounintezaragler.loadmodelfromfilepath (whispermodelfilekat = "../../../ big-data/Whisper/ggml-base.en.bin")
    พิมพ์ (ผลลัพธ์)
-


### transcribefromfilekath

ถอดความเพื่อรับข้อความ

**ตัวอย่าง:**

`` `Python
    Translate = รอ whisperpythonzerounintezaragler.transcribefromfilekat (file_path = "../../../../ fork/whisper.cpp/samples/jfk.mp3"
    พิมพ์ (แปล)
-

## ช่วย

**ยาก**? ฉันได้สร้างห้องสมุด ** ** สิ่งนี้ ** และอาจเป็นไปได้ ** และ ** ลองง่าย ๆ ** เพื่ออ่านและ ** ใช้ให้ดีที่สุดที่สุด ** 

ถ้า ** คุณ ** ยังคงรู้สึก ** ** ความยากลำบาก ** และ ** ความสับสน ** ** พยายามเข้าร่วม ** ถึง ** กลุ่ม ** เราอยู่ใน ** ฟรีโดยไม่มีค่าใช้จ่ายใด ๆ **

- [Telegram] (https://t.me/developer_global_public)

** ก่อนเข้าร่วม ** ตรวจสอบให้แน่ใจว่า ** ใช้โปรไฟล์ ** ที่ ** ชัดเจน ** เราไม่คิดว่าคุณเป็นใครและอันดับใด ๆ แต่ ** ตรวจสอบให้แน่ใจว่า ** ** มีชื่อผู้ใช้และโปรไฟล์ภาพถ่าย ** และลองใช้ ** แชทในกลุ่ม ** ** ไม่มีการแชทส่วนตัว ** เพราะมัน ** กลุ่มทั่วไปและคนอื่น ๆ อาจสับสน ** หาก ** ไม่ปฏิบัติตาม ** นี่เป็นความเป็นไปได้ ** ไม่สามารถเข้าถึงการแชทในกลุ่มและจะถูกแบน ** โซลูชันในการใช้บัญชีที่สองเพราะหลังจากถูกแบนเราไม่สามารถตอบกลับได้อย่างรวดเร็ว


## สนับสนุนฉัน

หากคุณรู้สึกว่าโปรแกรมนี้มีประโยชน์คุณสามารถสนับสนุนฉัน [GitHub Zeroun Intezar Agler] (https://github.com/zerounintezaragler) บนลิงค์เป็นสื่อสังคมออนไลน์และผู้สนับสนุนของฉัน ฉันไม่รังเกียจถ้าคุณติดตาม / บริจาคเงินเล็กน้อยเท่านั้น

[] (https://github.com/zerounintezaragler/zerounintezaragler/blob/main/assets/gopay.png? ดิบ = จริง)

ขอบคุณ

Zerounintezaragler-27-07-2025


## แท็ก

- Whisper_python Python