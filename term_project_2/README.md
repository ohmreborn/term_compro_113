สามารถโหลด Dataset ได้[ที่นี่](https://drive.google.com/uc?export=download&id=17Xasteq4XZChyaETA1ZNMYE4Zco3djzt)
โดยใน data ประกอบด้วย

* ImdbId : id ของหนัง
* _id : id ของหนัง
* name : ชื่อหนัง
* poster_url : url ของหนัง
* year : ปีที่ฉาย
* certificate : rate หนังมั้ง
* runtime : ความยาวหนัง
* genre : ประเภท
* ratingValue : เรทติง
* summary_text : เรื่องย่อ
* ratingCount : จำนวนคนให้คะแนน
* director : ผู้กำกับ
* cast : นักแสดง

จงสร้าง ฟังก์ชัน q1 กับ q2 โดยที่ 
* q1 5 อันดับ rating หนังที่มี Harrison Ford แสดงโดยไม่มี 'Steven Spielberg' เป็นผู้กำกับ
* q2 หนังที่ี Harrison Ford และ Tommy Lee Jones แสดงโดยไม่มี 'Steven Spielberg' และ George Lucas เป็นผู้กำกับ
```python
>>> q1()
Andrew Davis
Denis Villeneuve
Emily Goldberg
George Lucas
Irvin Kershner
Michel Parbot
Richard Marquand
Ridley Scott
Robert Guenette
Tony Miller
```

```python
>>> q2()
The Fugitive
```

> Note ไม่แนะนำให้เขียนโคดใน คอมพิวเตอร์ส่วนตัว เพราะมันจะค้าง
แนนำให้เขียน ใน google colab โดยใช้ไฟล์ submit.ipynb