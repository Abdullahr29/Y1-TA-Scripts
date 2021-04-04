
int x = 0;
float period = 30.0;
float pi = 3.1415927;


void setup(){
  Serial.begin(9600);
  for(int i = -10; i < 11; i++){
    Serial.print("-");
  }
  Serial.print("\n");
  
  
}


void printLine(float y){
  int funcPos = round(y*10);
  for(int i = -10; i < 11; i++){
    if(i == funcPos){
      Serial.print("*");
    }  
    else if(i == 0){
      Serial.print("|");
    }
    else{
      Serial.print(".");
    } 
  } 
}

void increment(int *var){
  int out = *var;
  out = out + 1;
  *var = out;
}

void loop(){
  float y = sin((2*pi/period)*x);
  x++;
  printLine(y);
  Serial.print("\n");
  //code to test increment pointer function
}
