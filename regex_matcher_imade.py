import re
import pandas as pd
def evalregex(final_bucket1,final_bucket2,path):
   da_list=[]
   sent_list=[]
   data=open(path,'r')
   print('Now going through the data to be evaluated')
   for line in data:
      #print(line)
      found=0
      list2b=[]
      sent_list.append(line)
      for pattern in final_bucket1:
         ends=pattern.split()
         if len(ends)>=2:
            regex=r' '+re.escape(ends[0])+r' (.+?) '+re.escape(ends[1])+r' '
            x=re.search(regex,line)
            if x:
               found=x.group(1)
               #print(found)

               list2b.append(found)
               break
      else:
         
         for pattern in final_bucket2:
            ends=pattern.split()
            if len(ends)>=2:
               regex=r' '+re.escape(ends[0])+r' '+re.escape(ends[1])+r' (.*) '
               x=re.search(regex,line)
               if x:
                  found=x.group(1)
                  #print(found)

                  list2b.append(found)
      if found==0:
         list2b.append('Not Found')

      da_list.append(list2b)
   #print(da_list)
   final_answer=zip(sent_list,da_list)
   #print(final_answer)
   fully_final_list=[list(l) for l in final_answer]

   print('Done going through evaluation data')


   #making the file
   for i in fully_final_list:

      t=open('output.txt','a')
      t.write('\n')
      x=i[0].split()
      s=' '.join(x)
      t.write(s+'\t'+i[1][0])
      t.write('\n')
      t.close()
   return(fully_final_list)
      
