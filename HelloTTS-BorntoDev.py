from gtts import gTTS
import playsound
tts = gTTS(text='เลิกทะเลาะกันเป็นเด็กได้แล้ว จาวิสเห็นแล้วเซงเลยอ่ะ ไม่น่าเกิดมาเลย ฮรือๆๆ ร้องไห้แล้ว', lang='th')
tts.save("helloWorld.mp3")
playsound.playsound("helloWorld.mp3", True)