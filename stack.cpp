#include<stdio.h>
#include<stdlib.h>

class stack{

private:
  struct ele{
  int num;
  struct ele * next; 
  };

struct ele * top;

public:

//default constructor
  stack()
  {
  top = new struct ele;
  top->num=0;
  top->next=NULL;
  }//stack

 
  ~stack()
  {
   struct ele * del;
   while(top != NULL)
   {
    del = top;
    top = top->next;
    free(del); 
   }//end of while
  //free(top);
  }//end of ~struct


void push(int newnum);
int pop(); 

};//end of class stack

void stack::push(int newnum)
{
  struct ele * newele;
  //newele = new struct ele;
  newele = (struct ele *)malloc(sizeof(struct ele));
  newele->num = newnum;
  newele->next = top;
  top = newele;
}

int stack::pop()
{
  int cur_num = top->num;
  struct ele * del;
  del = top;
  top = top->next;
  free(del);
  return(cur_num);
}

int main()
{
printf("hi\n");

stack a;
int i=100;

while(i!=10)
{
printf("\nEnter number:");
scanf("%d",&i);
a.push(i);
}
i=a.pop();
//printf("outside while: %d",i);


while(i!=0)
{
printf("%d\n",i);
i=a.pop();
}

return(1);
}
