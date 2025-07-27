# कानाफूसी अजगर

** कानाफूसी पायथन ** किसी भी ऑडियो से पाठ प्राप्त करें, बिना भुगतान किए, मुफ्त ऑफ़लाइन के लिए, GPU की कोई आवश्यकता नहीं है, और FFMPEG को बदलने की आवश्यकता नहीं है

- [[इंडोनेशिया] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme.md)
- 🇺🇸 [अंग्रेजी] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_en.md)
- [[कोरिया, दक्षिण कोरिया गणराज्य] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ko.md)
- 🇨🇳 [चीन] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_zh-cn.md)
- 🇿🇦 [दक्षिण अफ्रीका] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_af.md)
- [[भारत] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_hi.md)
- 🇯🇵 [जापान] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ja.md)
- 🇷🇺 [रूस] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ru.md)
- 🇹🇭 [थाईलैंड] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_th.md)
- 🇦🇪 [संयुक्त अरब अमीरात] (https://github.com/zerounintezaragler/whisper_python/blob/main/readme_ar.md)

## तथ्य

- यह पुस्तकालय कई निर्भरता 3 से बाध्य नहीं है
- FFMPEG की कोई आवश्यकता नहीं है

## विशेषता

- [x] ** बहुत तेज़ ** ASHNC लाइब्रेरी
- [x] ** का उपयोग करना आसान है **

## उदाहरण

- [सरल उदाहरण] (https://github.com/zerounintezaragler/whisper_python/tree/main/quickstart)

## स्थापित करना

स्थापित करने से पहले सुनिश्चित करें कि आप बुनियादी पायथन को जानते हैं कि कम से कम आपने अपने कंप्यूटर / डिवाइस पर Ptyhon स्थापित किया है। [पायथन वेबसाइट] (https://www.python.org)

- ** पायथन **

  `` `बैश
  पिप व्हिस्पर-पाइथॉन स्थापित करें
  `` `

## प्रलेखन

### सुनिश्चित करें

विधि को स्वतंत्र रूप से बुलाया जाना चाहिए ** के बाद ** / विधि से पहले ** पर ** पर ** लेकिन मैं ** पर ** से पहले सुझाव देता हूं

**उदाहरण:**

`` `पायथन
  Whisperpythonzerounintezaragler.ensureinitialized (लाइब्रेरीपैथ = "फोर्क/निर्भरता/lib/libwhisper_python.so")
`` `

### आरंभीकृत

इस विधि को ** पर ** विधि के बाद बुलाया जाना चाहिए क्योंकि अपडेट करने के लिए

**उदाहरण:**

`` `पायथन
  WISPERPYTHONZEROUNINTEZARAGLER.INITIALIZED () का इंतजार करें
`` `

### पर

यह विधि Invokes / अपडेट से डेटा अपडेट प्राप्त करने के लिए उपयोगी है

**उदाहरण:**

`` `पायथन

  def on_callback (अद्यतन: तानाशाही):
    प्रिंट (अद्यतन)

  Whisperpythonzerounintezaragler.on (event_name = "अद्यतन", on_callback = on_callback)
  
`` `


### LoadModelfromFilePath

सुनिश्चित करें कि आप पहले मॉडल को लोड करते हैं ताकि आप ट्रांसक्राइब कर सकें

**उदाहरण:**

`` `पायथन
    परिणाम = प्रतीक्षा करें व्हिस्पेरपोनजेरोन्टेज़ारैग्लर.लोडमोडेल्फ्रोमफाइलपैथ (व्हिस्परमोडफाइल्कैट = "../../../ बिग-डेटा/व्हिस्पर/जीजीएमएल-बसे.न.बिन")
    प्रिंट (परिणाम)
`` `


### Transcromfromfilekath

पाठ प्राप्त करने के लिए ट्रांसक्राइब करें

**उदाहरण:**

`` `पायथन
    अनुवाद = WISPERPYTHONZEROUNINTEZARAGLER.TRANSBRIBEFROMFILEKAT (FILE_PATH = "../../../../ Fork/Whisper.cpp/samples/jfk.mp3") का इंतजार करें।
    प्रिंट (अनुवाद)
`` `

## मदद

**कठिन**? मैंने ** लाइब्रेरी ** इस ** के साथ -साथ संभव ** हो सकता है और ** आसान ** पढ़ने के लिए आसान प्रयास किया है और ** जितना संभव हो उतना सबसे अच्छा उपयोग किया जाता है **। 

यदि ** आप ** अभी भी ** महसूस करते हैं ** ** ** कठिनाई ** और ** भ्रम ** ** ** ** से जुड़ने की कोशिश करें ** समूह ** हम ** बिना किसी लागत के ** मुक्त **

- [टेलीग्राम] (https://t.me/developer_global_public)

** शामिल होने से पहले ** सुनिश्चित करें ** प्रोफ़ाइल का उपयोग करें ** ** स्पष्ट ** स्पष्ट ** हमें कोई आपत्ति नहीं है कि आप कौन हैं, और कोई भी रैंक, लेकिन सुनिश्चित करें कि ** ** एक उपयोगकर्ता नाम और फोटो प्रोफ़ाइल है **, और समूह में ** चैट करने का प्रयास करें ** ** कोई व्यक्तिगत चैट ** ** क्योंकि यह ** सामान्य समूह और शायद अन्य लोग भ्रमित हैं **। यदि ** ** का पालन नहीं करता है तो यह संभावना है कि ** समूह में चैट नहीं एक्सेस नहीं कर सकता है और इसे प्रतिबंधित कर दिया जाएगा **, दूसरे खाते का उपयोग करने का समाधान, क्योंकि प्रतिबंधित होने के बाद हम जल्दी से जवाब नहीं दे सकते हैं


## मुझे समर्थन करो

यदि आपको लगता है कि यह कार्यक्रम उपयोगी है, तो आप मुझे [GitHub Zeroun Intezar Agler] (https://github.com/zerounintezaragler) का समर्थन कर सकते हैं, जो सोशल मीडिया और मेरे प्रायोजक उपलब्ध है। मुझे कोई आपत्ति नहीं है अगर आप केवल थोड़ा पैसा फॉलो / दान करते हैं

[] (https://github.com/zerounintezaragler/zeRounintezaragler/blob/main/assets/gopay.png? कच्चा = सच)

धन्यवाद

ZEROUNINTEZARAGLER-27-07-2025


## टैग

- व्हिस्पर_पिथन पायथन