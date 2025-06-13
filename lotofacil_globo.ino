#include <Servo.h>
#include <LiquidCrystal.h>

Servo servo;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int SENSOR_PIN = A0;
const int MOTOR_PIN = 6;
const int NUM_BOLAS  = 15;

bool bolaDetectada = false;
int contador = 0;

void setup() {
  pinMode(MOTOR_PIN, OUTPUT);
  analogWrite(MOTOR_PIN, 200);
  servo.attach(9);
  lcd.begin(16, 2);
  lcd.print("Lotofacil");
  delay(2000);
  lcd.clear();
}

void loop() {
  int sensorValue = analogRead(SENSOR_PIN);

  if (sensorValue > 500 && !bolaDetectada) {
    bolaDetectada = true;
    contador++;

    lcd.clear();
    lcd.print("Bola ");
    lcd.print(contador);

    servo.write(90);
    delay(500);
    servo.write(0);

    if (contador >= NUM_BOLAS) {
      analogWrite(MOTOR_PIN, 0);
      lcd.clear();
      lcd.print("Sorteio fim!");
      while (true);
    }
  } else if (sensorValue < 500) {
    bolaDetectada = false;
  }
}
