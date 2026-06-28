import sys
import json


class Log_Ext:
   '''
   Log_Extraction:
   # Extract 2 desired json argements from complex string containing you data
   # You can run it in your terminal and passing parameters you wish


   input_file:
       location in file system like: pwd appened file name
   output_file:
       contain results
   filed1:
       the json argement or name
       the 1st json argement you want
   field2:
       the 2ed
   '''
  
  
   def __init__(self, input_file, output_file, field1, field2):


       self.input_file = input_file
       self.output_file = output_file
       self.field1 = field1
       self.field2 = field2
      
  
   def parse_line(self, line:str):
       try:
           if "[MercLevelUp]" not in line:
               return None, 0
           json_start = line.index("{")
           gameStat = json.loads(line[json_start:])
           f1 = gameStat.get(self.field1)
           f2 = gameStat.get(self.field2, 0)
           return f1, f2
       except Exception:
           return None, 0


   def run(self):
       with open(self.input_file, "r") as f, open(self.output_file, "w") as output:
           for line in f:
               if "[MercLevelUp]" not in line:
                   continue
                      
               f1, f2 = self.parse_line(line)
               if f1 is not None:
                   output.write(f"{f1},{f2}\n")




if __name__ == "__main__":
   Ext = Log_Ext(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
   Ext.run()
