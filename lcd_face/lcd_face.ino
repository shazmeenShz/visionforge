#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

String data = "";
int smileCount = 0;
int sadCount = 0;
b
byte smiley[8] = {
  0b00000,
  0b01010,
  0b01010,
  0b00000,
  0b10001,
  0b01110,
  0b00000,
  0b00000
};

byte sadface[8] = {
  0b00000,
  0b01010,
  0b01010,
  0b00000,
  0b01110,
  0b10001,
  0b00000,
  0b00000
};

void setup() {
  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  lcd.createChar(0, smiley); 
  lcd.createChar(1, sadface); 

  lcd.setCursor(0, 0);
  lcd.print("Emotion Detect");
  lcd.setCursor(0, 1);
  lcd.print("Starting...");
  delay(2000);
  lcd.clear();
}

void loop() {
  if (Serial.available()) {
    data = Serial.readStringUntil('\n');

    int sIndex = data.indexOf("S:");
    int dIndex = data.indexOf("D:");

    if (sIndex != -1 && dIndex != -1) {
      smileCount = data.substring(sIndex + 2, data.indexOf(',', sIndex)).toInt();
      sadCount   = data.substring(dIndex + 2).toInt();

      lcd.clear();

    
      lcd.setCursor(0, 0);
      lcd.print("Smile ");
      lcd.write(byte(0)); 
      lcd.print("  ; ");
      lcd.print(smileCount);

    
      lcd.setCursor(0, 1);
      lcd.print("Sad ");
      lcd.write(byte(1));
      lcd.print("  ; ");
      lcd.print(sadCount);
    }
  }
}
