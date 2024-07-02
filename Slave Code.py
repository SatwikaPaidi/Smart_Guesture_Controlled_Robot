#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3); // RX, TX pins for HC-05 module

// Motor control pins
const int motor1A = 9;
const int motor1B = 8;
const int motor1E = 11;  // ENA Pin

const int motor2A = 7;
const int motor2B = 6;
const int motor2E = 10;  // ENB Pin

void setup() {
  // Initialize motor control pins as outputs
  pinMode(motor1A, OUTPUT);
  pinMode(motor1B, OUTPUT);
  pinMode(motor1E, OUTPUT);
  
  pinMode(motor2A, OUTPUT);
  pinMode(motor2B, OUTPUT);
  pinMode(motor2E, OUTPUT);
  
  // Initialize serial communication
  Serial.begin(9600);
  BTSerial.begin(9600);
}

void loop() {
  if (BTSerial.available()) { // Check if data is available to read from Bluetooth
    String receivedData = BTSerial.readStringUntil('\n'); // Read the incoming data
    Serial.println("Received data from master: " + receivedData); // Debug message to show received data
    
    // Extract pitch and roll angles from the received data
    float pitch = receivedData.substring(receivedData.indexOf("Pitch:") + 7, receivedData.indexOf(" degrees, Roll:")).toFloat();
    float roll = receivedData.substring(receivedData.indexOf("Roll:") + 6, receivedData.lastIndexOf(" degrees")).toFloat();

    // Print orientation
    Serial.print("Orientation: Pitch = ");
    Serial.print(pitch);
    Serial.print(" degrees, Roll = ");
    Serial.println(roll);

    // Determine the motion based on pitch and roll angles
    if (pitch > -90 && pitch < 0) {
      // Move forward
      forward();
    } else if (pitch > 0 && pitch < 90) {
      // Move backward
      backward();
    } else if (roll > 0 && roll < 90) {
      // Move right
      right();
    } else if (roll > -90 && roll < 0) {
      // Move left
      left();
    } else {
      // Stop
      stopMotors();
    }
  }
}

// Function to move motors forward
void forward() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  analogWrite(motor1E, 255);  // Full speed
  
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
  analogWrite(motor2E, 255);  // Full speed
  
  Serial.println("Moving Forward");
}

// Function to move motors backward
void backward() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, HIGH);
  analogWrite(motor1E, 255);  // Full speed
  
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, HIGH);
  analogWrite(motor2E, 255);  // Full speed
  
  Serial.println("Moving Backward");
}

// Function to move motors right
void right() {
  digitalWrite(motor1A, HIGH);
  digitalWrite(motor1B, LOW);
  analogWrite(motor1E, 255);  // Full speed
  
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, HIGH);
  analogWrite(motor2E, 255);  // Full speed
  
  Serial.println("Moving Right");
}

// Function to move motors left
void left() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, HIGH);
  analogWrite(motor1E, 255);  // Full speed
  
  digitalWrite(motor2A, HIGH);
  digitalWrite(motor2B, LOW);
  analogWrite(motor2E, 255);  // Full speed
  
  Serial.println("Moving Left");
}

// Function to stop motors
void stopMotors() {
  digitalWrite(motor1A, LOW);
  digitalWrite(motor1B, LOW);
  analogWrite(motor1E, 0);  // Stop
  
  digitalWrite(motor2A, LOW);
  digitalWrite(motor2B, LOW);
  analogWrite(motor2E, 0);  // Stop
  
  Serial.println("Motors Stopped");
}

